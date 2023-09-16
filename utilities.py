import sys
from datetime import date
from os.path import exists
import yaml
from yaml import SafeLoader


def config_file_generator():
    """Generate the template of config file"""
    with open('config.yml', 'w', encoding="utf8") as f:
        f.write("""# | Work_Log_Bot                 |
# | Made by KXX                          |
# ++------------------------------------++

# Your email account.
account: "default"

# Your email password.
password: "default"

# Your name.
name: "default"

# Who you want to send the work log to.
# Make the name or email address as the key.
receiver: "default"

# Who you want to send the carbon copy to.
# Use space to separate the name or email address.
carbon_copy: "default default default"

# The email title.
# MMDD <NAME>工作彙報
title: "default"

# The email content.
# Use space to separate the content.
content: "default default default"


# default Format :
# MMDD <NAME>工作彙報
#Dear All,
#
#今日工作內容為
#
#1. default
#2. default
#3. default
#
#以上如果有什麼問題再請各位提出來，謝謝。
#
#Best regards,
#Name

#------------------------------------


"""
                )
    sys.exit()


def read_config():
    """Read config file.
    Check if config file exists, if not, create one.
    if exists, read config file and return config with dict type.
    :rtype: dict
    """
    if not exists('./config.yml'):
        print("Config file not found, create one by default.\nPlease finish filling config.yml")
        with open('config.yml', 'w', encoding="utf8"):
            config_file_generator()

    try:
        with open('config.yml', 'r', encoding="utf8") as f:
            data = yaml.load(f, Loader=SafeLoader)
            config = {
                'account': data['account'],
                'password': data['password'],
                'name': data['name'],
                'receiver': data['receiver'],
                'carbon_copy': data['carbon_copy'],
                'title': data['title'],
                'content': data['content'],
            }
            return config
    except (KeyError, TypeError):
        print(
            "An error occurred while reading config.yml, please check if the file is corrected filled.\n"
            "If the problem can't be solved, consider delete config.yml and restart the program.\n")
        sys.exit()


def generate_numbered_work_log_with_spaces(content):
    """Generate numbered work log with spaces.
    :param content: The content of the work log.
    :return: The numbered work log with spaces.
    """
    items = content.split()
    numbered_content = ""
    line_number = 1

    for item in items:
        numbered_content += f"{line_number}. {item}\n"
        line_number += 1

    work_log = f"Dear All,\n\n今日工作內容為\n\n{numbered_content}\n以上如果有什麼問題再請各位提出來，謝謝。\n\nBest regards,\nKai"
    return work_log


def generate_title(name, title):
    """Generate the title of the email.
    :param name: The name of the receiver.
    :return: The title of the email.
    """
    if name == "default":
        print("Please fill in your name in config.yml")
        sys.exit()
    elif title == "default":
        today_date = date.today().strftime("%m%d")
        new_title = f"{today_date} <{name}>工作彙報"
        return new_title
    else:
        return title
