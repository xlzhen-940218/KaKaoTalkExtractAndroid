## 💬 KakaoTalk Chat Extractor (Rootless)

### 🇨🇳 中文

## 💬 KakaoTalk 聊天记录提取工具（免 Root）

这是一个 Python 脚本（`main.py`），用于在**不需要 Root 权限**的情况下，提取 Android 设备上的 KakaoTalk 聊天记录数据库（`KakaoTalk.db`）。

### 核心原理

本工具利用 Android 的 `adb backup` 功能。为了兼容性，它会执行以下步骤：

1.  **备份**官方 KakaoTalk APK。
2.  **卸载**官方版本（保留用户数据）。
3.  **安装**用户提供的旧版 `kakaotalk.apk`。
4.  **执行 `adb backup`**（此步骤需手动在手机上操作）。
5.  **恢复**官方 KakaoTalk 版本。
6.  **解密并解压**备份文件，提取加密的 `KakaoTalk.db`。

---

### ⚠️ 免责声明与风险提示

* **自行备份：** 本操作涉及应用卸载和安装，**请务必自行对手机数据进行完整备份。**
* **兼容性：** 本方法依赖于特定的旧版 APK 和 Android 系统的备份功能，**未来可能随时失效**。
* **风险自负：** 本项目仅供学习研究，作者不对任何数据丢失或设备损坏承担责任。

---

### 🚀 准备工作（运行前必读）

| **要求** | **说明** |
| :--- | :--- |
| **ADB 工具** | 确保系统已安装 ADB 并配置了环境变量。 |
| **Java 环境** | 运行 `abp.jar`（用于解密备份文件）需要 Java 运行时环境（JRE/JDK）。 |
| **手机设置** | 开启 **USB 调试**，并通过 USB 连接电脑并授权。 |
| **文件清单** | 以下所有文件必须**位于脚本运行的同一目录下**：`main.py`、`kakaotalk.apk` (旧版)、`abp.jar`、`7z.exe`。 |

### 💻 运行步骤

1.  **执行脚本：** 打开命令行，运行 `python main.py`。
2.  **手机操作（关键步骤）：**
    * 当脚本提示时，请留意你的手机屏幕。手机会弹出 **“完整备份”** 提示。
    * **重要：** 在手机上输入备份密码 `0000` 并确认开始备份。
3.  **提取完成：** 脚本运行结束后，加密的 `KakaoTalk.db` 文件将位于：
    `kakao_data/kakaotalk/apps/com.kakao.talk/db/KakaoTalk.db`

### 🎉 后续步骤：解密数据库

**提取到的 `KakaoTalk.db` 文件是加密的**，你需要使用第三方工具对其进行解密，才能用 SQLite 工具查看聊天记录。

请使用以下工具进行解密：

* **解密工具：** [jiru/kakaodecrypt](https://github.com/jiru/kakaodecrypt)

请遵循该 GitHub 项目提供的说明，解密数据库文件。

---

### 🇬🇧 English

## 💬 KakaoTalk Chat Extractor (Rootless)

This is a Python script (`main.py`) designed to extract the KakaoTalk chat database (`KakaoTalk.db`) from an Android device **without requiring root access**.

### Core Mechanism

The tool leverages Android's built-in `adb backup` functionality. To ensure compatibility, it follows this sequence:

1.  **Backs up** the official KakaoTalk APKs.
2.  **Uninstalls** the official version (preserving user data).
3.  **Installs** a user-provided older `kakaotalk.apk`.
4.  **Executes `adb backup`** (requires manual input on the phone).
5.  **Restores** the official KakaoTalk version.
6.  **Decrypts and Unpacks** the backup file to retrieve the encrypted `KakaoTalk.db`.

---

### 🚀 Pre-requisites (Must Read Before Running)

| **Requirement** | **Details** |
| :--- | :--- |
| **ADB Tools** | Ensure ADB is installed and configured on your system. |
| **Java Environment** | Java (JRE/JDK) is needed for `abp.jar` (used to decrypt backup files). |
| **Phone Setup** | **Enable USB Debugging**, connect your phone via USB, and authorize the connection. |
| **File Checklist** | **All files must be in the same running directory:** `main.py`, `kakaotalk.apk` (old version), `abp.jar`, and `7z.exe`. |

### 💻 Execution Steps

1.  **Run Script:** Open your command line and execute `python main.py`.
2.  **Phone Interaction (Crucial):**
    * When prompted, look at your phone screen. A **"Full backup"** screen will pop up.
    * **CRITICAL:** On your phone, enter the backup password `0000` and confirm to start the backup.
3.  **Extraction Complete:** Once the script finishes, the encrypted `KakaoTalk.db` file will be located at:
    `kakao_data/kakaotalk/apps/com.kakao.talk/db/KakaoTalk.db`

### 🎉 Next Step: Decrypting the Database

The **extracted `KakaoTalk.db` file is encrypted**. You must use a third-party tool to decrypt it before you can view the chat history using a standard SQLite viewer.

Please use the following tool for decryption:

* **Decryption Tool:** [jiru/kakaodecrypt](https://github.com/jiru/kakaodecrypt)

Follow the instructions provided in the GitHub repository to decrypt your database file.

---

### 🇰🇷 한국어 (Korean)

## 💬 카카오톡 채팅 기록 추출 도구 (루트 불필요)

이 Python 스크립트(`main.py`)는 **루트 권한 없이** Android 기기에서 카카오톡 채팅 데이터베이스(`KakaoTalk.db`)를 추출하도록 설계되었습니다.

### 핵심 작동 원리

이 도구는 Android의 기본 `adb backup` 기능을 활용합니다. 호환성을 위해 다음과 같은 단계를 따릅니다.

1.  공식 카카오톡 APK 파일을 **백업**합니다.
2.  공식 버전을 **제거**합니다 (사용자 데이터는 보존).
3.  사용자가 제공한 구버전 `kakaotalk.apk`를 **설치**합니다.
4.  **`adb backup`을 실행합니다** (이 단계는 휴대폰에서 수동 입력이 필요합니다).
5.  공식 카카오톡 버전을 **복구**합니다.
6.  백업 파일을 **복호화 및 압축 해제**하여 암호화된 `KakaoTalk.db`를 추출합니다.

---

### 🚀 필수 준비 사항 (실행 전 필독)

| **요구 사항** | **설명** |
| :--- | :--- |
| **ADB 도구** | 시스템에 ADB가 설치 및 구성되어 있는지 확인하세요. |
| **Java 환경** | `abp.jar` (백업 파일 복호화에 사용) 실행을 위해 Java (JRE/JDK)가 필요합니다. |
| **휴대폰 설정** | **USB 디버깅을 활성화**하고, USB로 컴퓨터에 연결한 후 승인하세요. |
| **파일 목록** | 다음 모든 파일은 **스크립트 실행 폴더와 동일한 위치**에 있어야 합니다: `main.py`, `kakaotalk.apk` (구버전), `abp.jar`, `7z.exe`. |

### 💻 실행 단계

1.  **스크립트 실행:** 명령줄을 열고 `python main.py`를 실행합니다.
2.  **휴대폰 조작 (핵심 단계):**
    * 스크립트에서 메시지가 표시되면 휴대폰 화면을 확인하세요. **"전체 백업(Full backup)"** 화면이 나타납니다.
    * **중요:** 휴대폰에서 백업 비밀번호로 `0000`을 입력하고 백업 시작을 확인하세요.
3.  **추출 완료:** 스크립트 실행이 완료되면, 암호화된 `KakaoTalk.db` 파일은 다음 위치에 있습니다.
    `kakao_data/kakaotalk/apps/com.kakao.talk/db/KakaoTalk.db`

### 🎉 다음 단계: 데이터베이스 복호화

**추출된 `KakaoTalk.db` 파일은 암호화되어 있습니다.** 표준 SQLite 뷰어를 사용하여 채팅 기록을 보려면 타사 도구를 사용하여 복호화해야 합니다.

복호화를 위해 다음 도구를 사용하십시오.

* **복호화 도구:** [jiru/kakaodecrypt](https://github.com/jiru/kakaodecrypt)

해당 GitHub 프로젝트에 제공된 지침에 따라 데이터베이스 파일을 복호화하십시오.
