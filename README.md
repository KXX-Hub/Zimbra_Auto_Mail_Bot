# Zimbra Auto Mail Bot
## Description
This is a simple bot that can send emails to multiple recipients Which is made by python selenium.
## How to use
### requirements
- python 3.8
- selenium
- webdriver
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

content_format:
  work_log_header: "Dear All,


今日工作內容為


"

  line_number_prefix: "{line_number}."
  work_log_footer: "
  
  
以上如果有什麼問題再請各位提出來，謝謝。

Best regards,

"
  signature: "{name}"
```
### default format
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
1. Clone this repository or download the [latest release](https://github.com/KXX-Hub/Line_Gas_Notify/releases)
2. Install all in requirements.txt
3. Run main.py first time to get config.yml
4. Edit config.yml(use **&** to separate account and content)
5. Run main.py
