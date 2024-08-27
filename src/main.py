from ConfigRetriever import ConfigRetriever
from ZimbraDriver import ZimbraDriver
from MailGenerator import MailGenerator
import shutil
import os

def CheckFileExist():
    notFound = ""
    if not os.path.exists("./config.yml"):
        ConfigRetriever().GenerateConfig()
        notFound += "'config.yml'"
    if not os.path.exists("./content.txt"):
        MailGenerator.GenerateTxt()
        if notFound != "":
            notFound += " & "
        notFound += "'content.txt'"
    if notFound != "":
        raise FileNotFoundError(f"{notFound} not found.\nThe system has automatically generated one.\nPlease fill in and restart the program.")

def GetSeperator():
    column, _ = shutil.get_terminal_size()
    return "=" * column
if __name__ == "__main__":
    try:
        CheckFileExist()
        configInfo = ConfigRetriever()
        config = configInfo.GetConfig()
        ZimbraDriver(config).Execute()
    except Exception as e:
        seperator = GetSeperator()
        print(seperator)
        print(f"\n{e}\n")
        print(seperator)
