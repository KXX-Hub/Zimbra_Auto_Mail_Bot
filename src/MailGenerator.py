from typing import Dict
from datetime import datetime
import os

class MailGenerator():
    def __init__(self, config: Dict[str, str]) -> None:
        self._config = config

    def GetContent(self) -> str:
        if os.path.exists("./content.txt"):
            with open("./content.txt", "r", encoding="utf-8") as file:
                content = file.read()
            return content
        else:
            self.GenerateTxt()
            path = self._config["ContentPath"]
            raise FileNotFoundError(f"'{path}' was not found.\nThe system has automatically generated one.\nPlease complete the contents and restart the program.")
    
    def GetTitle(self) -> str:
        title = self._config["Title"]
        title = title.replace("{NAME}", self._config["Name"])
        title = title.replace("{DATE}", datetime.today().strftime("%Y%m%d"))
        return title
    
    def GetReceiever(self) -> str:
        return self._config["Receiver"]
    
    @staticmethod
    def GenerateTxt():
        with open("./content.txt", "w", encoding="utf-8") as file:
            file.writelines("在此放入您想寄出的內容")
        