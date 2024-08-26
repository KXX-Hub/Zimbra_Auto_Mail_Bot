from typing import Dict
from typing import Tuple
import time
import shutil
from MailGenerator import MailGenerator
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class ZimbraDriver():
    def __init__(self, config:Dict[str, str]) -> None:
        self._config = config
        self._mailGenerator = MailGenerator(config)
        self.InitializeChromeDriver()

    def __del__(self) -> None:
        time.sleep(3)
        self._driver.close()

    def Execute(self):
        if self.Confirm():
            self.Login()
            self.SendEmail()
        else:
            pass

    def Login(self):
        url = "https://mail.gss.com.tw/zimbra"
        self._driver.get(url)
        self._driver.maximize_window()
        self.DriverSendKeys((By.XPATH, '//*[@id="username"]'), self._config["Account"])
        self.DriverSendKeys((By.XPATH, '//*[@id="password"]'), self._config["Password"])
        self.DriverClick((By.XPATH, '/html/body/div/div[1]/div[1]/form/table/tbody/tr[3]/td[2]/input[2]'))

    def SendEmail(self):
        self.DriverClick((By.XPATH, '//*[@id="zb__NEW_MENU_title"]'))
        composeVersion = self.DetermineComposeVersion()
        for receiver in self._config["Receiver"].split("&"):
            receiver = receiver.strip()
            self.DriverSendKeys((By.XPATH, f'//*[@id="zv__COMPOSE-{composeVersion}_to_control"]'), receiver)
            self.DriverSendKeys((By.XPATH, f'//*[@id="zv__COMPOSE-{composeVersion}_to_control"]'), Keys.ENTER)
        for cc in self._config["CarbonCopy"].split("&"):
            cc = cc.strip()
            self.DriverSendKeys((By.XPATH, f'//*[@id="zv__COMPOSE-{composeVersion}_cc_control"]'), cc)
            self.DriverSendKeys((By.XPATH, f'//*[@id="zv__COMPOSE-{composeVersion}_cc_control"]'), Keys.ENTER)
        self.DriverSendKeys((By.XPATH, f'//*[@id="zv__COMPOSE-{composeVersion}_subject_control"]'), self._mailGenerator.GetTitle())
        self.DriverSendKeys((By.XPATH, f'//*[@id="zv__COMPOSE-{composeVersion}_subject_control"]'), Keys.ENTER)
        if self._config["HasSignature"]:
            self._driver.switch_to.frame(0)
            self.DriverClear((By.XPATH, '//*[@id="tinymce"]/div[1]'))
            self.DriverSendKeys((By.XPATH, '//*[@id="tinymce"]/div[1]'), f"{self._mailGenerator.GetContent()}\n")
            time.sleep(1)
            self._driver.switch_to.default_content()
        else:
            self.DriverSendKeys((By.XPATH, f'//*[@id="ZmHtmlEditor{composeVersion}_body"]'), self._mailGenerator.GetContent())
        self.DriverClick((By.XPATH, '//*[@id="zb__COMPOSE-1__SEND_MENU_title"]'))
        

    # html內的數字可能會變，所以要先找到該次啟動時數字是多少
    def DetermineComposeVersion(self):
        for i in range(10000):
            elements = self._driver.find_elements(By.XPATH, f'//*[@id="zv__COMPOSE-{i}_to_control"]')
            if elements:
                return i

    def InitializeChromeDriver(self):
        options = webdriver.ChromeOptions()
        prefs = {'profile.default_content_setting_values': {'notifications': 2}}
        options.add_experimental_option('prefs', prefs)
        options.add_argument("--disable-infobars")
        self._driver = webdriver.Chrome(options=options)

    def DriverClick(self, locator:Tuple[str, str]):
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located(locator)).click()

    def DriverSendKeys(self, locator:Tuple[str, str], key:str):
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located(locator)).send_keys(key)

    def DriverClear(self, locator:Tuple[str, str]):
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located(locator)).clear()

    def Confirm(self):
        column, _ = shutil.get_terminal_size()
        seperator = "=" * column
        print("Previewing the email:")
        print(seperator)
        print("Receiver:\t" + self._config["Receiver"])
        print("Carbon copy: \t" + self._config["CarbonCopy"])
        print("Title: \t\t" + self._mailGenerator.GetTitle())
        print("Name: \t\t" + self._config["Name"])
        print("Content: \n\n" + self._mailGenerator.GetContent())
        print(seperator)
        while True:
            confirmSend = input("Do you want to send the email? (Y/N): ").strip().upper()
            if confirmSend == "Y":
                return True
            elif confirmSend == "N":
                return False
            else:
                print("Unknown Value. Please type Y or N")
