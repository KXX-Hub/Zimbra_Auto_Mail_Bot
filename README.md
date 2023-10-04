# Zimbra Auto Mail Bot
📖[中文版README.md](#Zimbra 自動寄信機器人)📖
## Description
This is a simple bot that can send emails to multiple recipients Which is made by python selenium.
<img width="450" src="./readme_imgs/front cover.jpg">
## How to use
### Requirements
>- selenium==4.11.2
>- PyYAML==6.0.1
### About Config
```
account: "Your email account"

password: "Your email password"

name: "Your name"

# Who you want to send the work log to.
# Make the name or email address as the key.
receiver: ""

# Who you want to send the carbon copy to.
# Use "&" to separate the name or email address.
carbon_copy: ""

# The email title.
# default: MMDD <NAME>工作彙報
# {DATE} and {NAME} will be auto-replaced by the date and your name.
title: "{DATE} <{NAME}> 工作彙報"

# If you have a signature, set it to True.
# If not, set it to False.
had_signatures: "False"
```
### Default Format
```
MMDD <NAME>工作彙報
Dear All,

今日工作內容為

1. default
2. default
3. default

以上如果有什麼問題再請各位提出來，謝謝。

Best regards,
Name
```
### How to run
> 1. Clone this repository or download the [latest release](https://github.com/KXX-Hub/Line_Gas_Notify/releases)
> 2. Install all pakages in requirements.txt
> 3. Edit config.yml (If don't have, **run main.py** and it will auto create one.)
> 4. Run main.py and enter the content of the email.(use **&** to separate account and content)
> 5. Enjoy the fast email sending.


## Contributing to the Project

### How to Contribute

1. Fork this project.
2. Clone your forked project to your local machine.
3. Create a new branch.
4. Contribute your code.
5. Commit/Push your code.
6. Create a new Pull Request.
7. Wait for a response.

### Code Writing/Commit Guidelines

* Keep each line under 100 characters.
* Use `snake_case` for variable and function names.
* Add a trailing blank line at the end of files.
* Optimize code and remove unnecessary imports.
* Use the following format for commit messages and write them in English:
    >- Update - your commit messages here
    >- Fix bug - your commit messages here
    >- Optimize - your commit messages here
    >- Standardize - your commit messages here

### Suggestions/Issue Reporting

If you have any suggestions or discover any issues, please submit your feedback in the [Issues](https://github.com/KXX-Hub/Zimbra_Auto_Mail_Bot/issues)
section, and I will respond as soon as possible!

# Zimbra 自動寄信機器人
📖[英文版README.md](#Zimbra Auto Mail Bot)📖
## 簡介
這是一個可以使用Python Selenium向多個收件人發送電子郵件的簡單機器人，提供你更快速的寄信體驗。
<img width="450" src="./readme_imgs/front cover.jpg">
## 如何使用
### requirements
selenium==4.11.2
PyYAML==6.0.1
### 關於Config
```
account: "您的電子郵件帳戶"
password: "您的電子郵件密碼"
name: "您的姓名"
receiver: ""  # 您要發送工作日誌的收件人。
carbon_copy: ""  # 您要副本抄送的人。
title: "{DATE} <{NAME}> 工作報告"  # 電子郵件標題。
had_signatures: "False"  # 如果您有簽名，請將其設置為True。如果沒有，請將其設置為False。
```
### 初始格式
```
MMDD <NAME>工作彙報
Dear All,

今日工作內容為

1. default
2. default
3. default

以上如果有什麼問題再請各位提出來，謝謝。

Best regards,
Name
```
### 如何執行

>1. Clone 此 repo或下載[最新版本](https://github.com/KXX-Hub/Line_Gas_Notify/releases)。
>2. 安裝requirements.txt中的所有packages。
>3. 編輯config.yml（若沒有，請運行main.py自動創建一個）。
>4. 運行main.py，並輸入電子郵件的內文（使用 **&** 分隔帳戶和內容）。
>5. 享受超高速傳送電子郵件。

## 貢獻
### 如何貢獻

1. Fork這個專案。 
2. 將您的Fork專案克隆到本地計算機。 
3. 建立一個新的分支。 
4. 貢獻您的代碼。 
5. 提交/推送您的代碼。 
6. 建立一個新的Pull Request。 
7. 等待回覆。

### Code Writing/Commit 規則
* 每行不超過100個字符。
* 變數和函數名稱使用snake_case。
* 在文件末尾添加一個空行。
* 優化代碼並刪除不必要的導入。
* 使用以下格式編寫提交消息並以英語撰寫：
>- Update - 在此處寫入您的提交消息
>- Fix bug - 在此處寫入您的提交消息
>- Optimize - 在此處寫入您的提交消息
>- Standardize - 在此處寫入您的提交消息

### 建議/問題報告
如果您有任何建議或發現任何問題，請在[Issues](https://github.com/KXX-Hub/Zimbra_Auto_Mail_Bot/issues)提交您的反饋，我會盡快回覆！