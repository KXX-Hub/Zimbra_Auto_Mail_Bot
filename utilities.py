import msvcrt
import sys
from datetime import date
from os.path import exists
import yaml
from yaml import SafeLoader


def config_file_generator():
    """Generate the template of config file"""
    with open('config.yml', 'w', encoding="utf8") as f:
        f.write("""# | Zimbra_Auto_Mail_Bot                |
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
# Use "&" to separate the name or email address.
carbon_copy: "default&default&default"

# The email title.
# MMDD <NAME>工作彙報
title: "default"

# If you have a signature, set it to true.
had_signatures: false

content_format:
  work_log_header: "Dear All,\n\n\n今日工作內容為\n\n\n"
  line_number_prefix: "{line_number}."
  work_log_footer: "\n\n以上如果有什麼問題再請各位提出來，謝謝。\n\nBest regards,\n\n"
  signature: "{name}"

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
                'content_format': data['content_format'],
                'had_signatures': data['had_signatures']
            }
            return config
    except (KeyError, TypeError):
        print(
            "An error occurred while reading config.yml, please check if the file is corrected filled.\n"
            "If the problem can't be solved, consider delete config.yml and restart the program.\n")
        sys.exit()


# def wait_for_enter_or_esc():
#     """Wait for enter or esc key.
#     :return: True if enter key is pressed, False if esc key is pressed.
#     """
#     while True:
#         key = msvcrt.getch()
#         if key == b'\r':  # Enter
#             return True
#         elif key == b'\x1b':  # Esc
#             return False


def generate_numbered_work_log(content):
    """Generate numbered work log with spaces.
    :param content: The content of the work log.
    :return: The numbered work log with &.
    """
    global work_log
    config = read_config()
    items = content.split("&")
    numbered_content = ""
    line_number = 1

    if isinstance(config["content_format"], dict):

        work_log_format = config["content_format"]
        work_log_header = work_log_format.get("work_log_header", "")
        work_log_footer = work_log_format.get("work_log_footer", "")
        line_number_prefix = work_log_format.get("line_number_prefix", "")
        had_signatures = config.get("had_signatures")
        name = config["name"]
    else:

        work_log_header = config.get("work_log_header", "")
        work_log_footer = config.get("work_log_footer", "")
        line_number_prefix = config.get("line_number_prefix", "")
        name = config["name"]
        had_signatures = config.get("had_signatures")

    for item in items:
        line_prefix = line_number_prefix.format(line_number=line_number)
        numbered_content += f"{line_prefix}{item}\n"
        line_number += 1
    if had_signatures:
        work_log = f"{work_log_header}{numbered_content}"
    if not had_signatures:
        work_log = f"{work_log_header}{numbered_content}{work_log_footer}{name}\n"
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
