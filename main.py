# This is a sample Python script.
import os
import tarfile
import time

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

android_device = ''
kakao_package_name = 'com.kakao.talk'


# read android device please open usb debug
def read_android_device():
    result = os.popen('adb devices').read()
    if result.__contains__('\tdevice'):
        results = result.split('\n')
        global android_device
        android_device = results[1].split('\t')[0]
        print('connected android device : {0}'.format(android_device))
        return True
    else:
        print('device not found! please usb connect device and open usb debug')
        return False


# backup kakao official apk ,program exited before re-install
def backup_kakao_official_apk():
    result = os.popen('adb -s {0} shell "pm path {1}"'.format(android_device, kakao_package_name)).read()
    results = result.split('\n')
    for line in results:
        if line.__contains__('package:'):
            path = line.split('package:')[1]
            if not os.path.exists('kakao_apks'):
                os.mkdir('kakao_apks')
            print('copy split apk...')
            os.system('adb -s {0} pull {1} kakao_apks/'.format(android_device, path))
    return os.listdir('kakao_apks').__len__() > 0


# uninstall kakaotalk official apk wait install old version kakaotalk
def uninstall_kakaotalk_with_out_data():
    result = os.popen('adb -s {0} shell pm uninstall -k {1}'.format(android_device, kakao_package_name)).read()
    return result.__contains__("Success")


# install old version kakao talk if failed need reboot system and retry
def install_old_version_kakaotalk():
    result = os.popen('adb -s {0} install -r -d {1}'.format(android_device, 'kakaotalk.apk')).read()
    return result.__contains__("Success")


# if install old version failed ,need reboot system
def reboot_system():
    os.system('adb -s {0} reboot'.format(android_device))
    time.sleep(15)  # sleep 15 seconds wait rebooting


# backup kakao talk data
def backup_kakao_talk_data():
    os.system('adb -s {0} shell am start -n {1}/.activity.SplashActivity'.format(android_device, kakao_package_name))
    print('Please look your phone and click continue...')
    time.sleep(5)
    if not os.path.exists('kakao_data'):
        os.mkdir('kakao_data')
    print('Please look your phone and input backup password 0000')
    os.system('adb -s {0} backup -f kakao_data/kakaotalk.ab com.kakao.talk'.format(android_device))
    return os.path.exists('kakao_data/kakaotalk.ab')


# backed data after re-install official apks
def install_official_apks():
    files = os.listdir('kakao_apks')
    apks = ''
    for file in files:
        apks = apks + ' kakao_apks/' + file
    os.system('adb -s {0} install-multiple  -r -d --user 0 {1}'.format(android_device, apks))


# unpack ab data
def unpack_ab_data():
    os.system('java -jar abp.jar unpack kakao_data/kakaotalk.ab kakao_data/kakaotalk.tar 0000 ')
    if os.path.exists('kakao_data/kakaotalk.tar'):
        os.system('7z.exe x "kakao_data/kakaotalk.tar" -o"kakao_data/kakaotalk" -r -y')
        return True
    else:
        return False


if __name__ == '__main__':

    connected = read_android_device()
    if connected:
        backed_apks = backup_kakao_official_apk()
        if backed_apks:
            uninstalled = uninstall_kakaotalk_with_out_data()
            if uninstalled:
                install_old_version = install_old_version_kakaotalk()
                while not install_old_version:
                    reboot_system()
                    install_old_version = install_old_version_kakaotalk()
                backed_data = backup_kakao_talk_data()
                install_official_apks()
                if backed_data:
                    unpacked = unpack_ab_data()
                    if unpacked:
                        print('unpack success!')
                        db_path = os.path.abspath('kakao_data/kakaotalk/apps/com.kakao.talk/db/KakaoTalk.db')
                        os.system('explorer.exe /e,/select, "{0}"'.format(db_path))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
