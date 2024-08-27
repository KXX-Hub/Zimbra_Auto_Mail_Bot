from os.path import exists
import yaml
from yaml import SafeLoader

class ConfigRetriever:

    def __init__(self):
        self.configPath = "./config.yml"

    def GetConfig(self):
        if exists(self.configPath) :
            return self.ReadConfig()
        else:
            self.GenerateConfig()
            raise FileNotFoundError("The 'config.yml' file was not found.\nThe system has automatically generated one.\nPlease complete the parameters and restart the program.")

    def ReadConfig(self):
        with open(self.configPath, "r", encoding="utf8") as file:
            data = yaml.load(file, Loader=SafeLoader)
            config = {
                'Account': data['account'],
                'Password': data['password'],
                'Name': data['name'],
                'Receiver': data['receiver'],
                'CarbonCopy': data['carbon_copy'],
                'Title': data['title'],
                'HasSignature': self.CheckBool(data['has_signature'])
            }
            return config
        
    def GenerateConfig(self):
        with open(self.configPath, 'w', encoding="utf8") as f:
            defaultFormat = "# ++------------------------------------++\n"
            defaultFormat += "# ++------------------------------------++\n"
            defaultFormat += "# | Zimbra_Auto_Mail_Bot               |\n"
            defaultFormat += "# | Made by KXX & VH                   |\n"
            defaultFormat += "# ++------------------------------------++\n"
            defaultFormat += "\n"
            defaultFormat += "# Your email account.\n"
            defaultFormat += "account: \n"
            defaultFormat += "\n"
            defaultFormat += "# Your email password.\n"
            defaultFormat += "password: \n"
            defaultFormat += "\n"
            defaultFormat += "# Your name.\n"
            defaultFormat += "name: default\n"
            defaultFormat += "\n"
            defaultFormat += "# Who you want to send the work log to.\n"
            defaultFormat += "# Make the name or email address as the key.\n"
            defaultFormat += "receiver: default\n"
            defaultFormat += "\n"
            defaultFormat += "# Who you want to send the carbon copy to.\n"
            defaultFormat += "# Use \"&\" to separate the name or email address.\n"
            defaultFormat += "# example : \"default&default&default\"\n"
            defaultFormat += "carbon_copy: \n"
            defaultFormat += "\n"
            defaultFormat += "# The email title.\n"
            defaultFormat += "# default: MMDD <NAME> 工作彙報\n"
            defaultFormat += "# {DATE} and {NAME} will be auto-replaced by the date and your name.\n"
            defaultFormat += "title: \"{DATE} <{NAME}> 工作彙報\"\n"
            defaultFormat += "\n"
            defaultFormat += "# If you have a signature, set it to True.\n"
            defaultFormat += "# If not, set it to False.\n"
            defaultFormat += "has_signature: False\n"
            defaultFormat += "\n"
            defaultFormat += "# default Format :\n"
            defaultFormat += "# YYYYMMDD <NAME> 工作彙報\n"
            defaultFormat += "# <Your content in txt>\n"
            defaultFormat += "\n"
            defaultFormat += "#------------------------------------\n"
            f.write(defaultFormat)


    def CheckBool(self, string:str):
        string = str(string)
        if string.upper() == "TRUE":
            return True
        elif string.upper() == "FALSE":
            return False
        else:
            raise ValueError(f"Unknown Value of 'has_signature': {string}")
        