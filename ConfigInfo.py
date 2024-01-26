from os.path import exists
from utilities import Utilities
import yaml
from yaml import SafeLoader

class ConfigInfo:

    def __init__(self):
        self.IsConfigExist()
        self.configPath = "./config.yml"

    def IsConfigExist(self):
        if exists(self.configPath) :
            self.ReadConfig()
        else:
            self.GenerateConfig()

    def ReadConfig(self):
        # TODO error exception
        with open(self.configPath, "r", encoding="utf8") as file:
            data = yaml.load(file, Loader=SafeLoader)
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
        
    def GenerateConfig(self):
        # TODO print messages
        with open(self.configPath, 'w', encoding="utf8") as f:
            defaultFormat = "# ++------------------------------------++\n"
            defaultFormat += "# ++------------------------------------++\n"
            defaultFormat += "# | Zimbra_Auto_Mail_Bot               |\n"
            defaultFormat += "# | Made by KXX                        |\n"
            defaultFormat += "# ++------------------------------------++\n"
            defaultFormat += "\n"
            defaultFormat += "# Your email account.\n"
            defaultFormat += "account: \"default\"\n"
            defaultFormat += "\n"
            defaultFormat += "# Your email password.\n"
            defaultFormat += "password: \"default\"\n"
            defaultFormat += "\n"
            defaultFormat += "# Your name.\n"
            defaultFormat += "name: \"default\"\n"
            defaultFormat += "\n"
            defaultFormat += "# Who you want to send the work log to.\n"
            defaultFormat += "# Make the name or email address as the key.\n"
            defaultFormat += "receiver: \"default\"\n"
            defaultFormat += "\n"
            defaultFormat += "# Who you want to send the carbon copy to.\n"
            defaultFormat += "# Use \"&\" to separate the name or email address.\n"
            defaultFormat += "# example : \"default&default&default\"\n"
            defaultFormat += "carbon_copy: \"\"\n"
            defaultFormat += "\n"
            defaultFormat += "# The email title.\n"
            defaultFormat += "# default: MMDD <NAME>工作彙報\n"
            defaultFormat += "# {DATE} and {NAME} will be auto-replaced by the date and your name.\n"
            defaultFormat += "title: \"{DATE} <{NAME}> 工作彙報\"\n"
            defaultFormat += "\n"
            defaultFormat += "# If you have a signature, set it to True.\n"
            defaultFormat += "# If not, set it to False.\n"
            defaultFormat += "had_signatures: \"False\"\n"
            defaultFormat += "\n"
            defaultFormat += "content_format:\n"
            defaultFormat += "  work_log_header: \"Dear All,\n\n\n今日工作內容為\n\n\n\"\n"
            defaultFormat += "  line_number_prefix: \"{line_number}.\"\n"
            defaultFormat += "  work_log_footer: \"\n\n以上如果有什麼問題再請各位提出來，謝謝。\n\nBest regards,\n\n\"\n"
            defaultFormat += "  signature: \"{name}\"\n"
            defaultFormat += "\n"
            defaultFormat += "# default Format :\n"
            defaultFormat += "# MMDD <NAME>工作彙報\n"
            defaultFormat += "#Dear All,\n"
            defaultFormat += "#\n"
            defaultFormat += "#今日工作內容為\n"
            defaultFormat += "#\n"
            defaultFormat += "#1. default\n"
            defaultFormat += "#2. default\n"
            defaultFormat += "#3. default\n"
            defaultFormat += "#\n"
            defaultFormat += "#以上如果有什麼問題再請各位提出來，謝謝。\n"
            defaultFormat += "#\n"
            defaultFormat += "#Best regards,\n"
            defaultFormat += "#Name\n"
            defaultFormat += "\n"
            defaultFormat += "#------------------------------------\n"
            f.write(defaultFormat)
            Utilities.ShutdownAfterXSecond(3)