from datetime import date

from selenium.common import TimeoutException

import utilities as utils
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

url = "https://mail.gss.com.tw/zimbra"
options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=options)
config = utils.read_config()
account = config.get('account')
password = config.get('password')
name = config.get('name')
receiver = config.get('receiver')
carbon_copy = config.get('carbon_copy').split()
title = config.get('title')
content = config.get('content')


def driver_click(locator):
    """Click the element.
    :param locator: The locator of the element.
    """
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator)).click()


def driver_send_keys(locator, key):
    """Send keys to element.
    :param locator: Locator of element.
    :param key: Keys to send.
    """
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator)).send_keys(key)


def login():
    driver.get(url)
    driver.maximize_window()
    driver_send_keys((By.XPATH, '//*[@id="username"]'), account)
    driver_send_keys((By.XPATH, '//*[@id="password"]'), password)
    driver_click((By.XPATH, '/html/body/div/div[1]/div[1]/form/table/tbody/tr[3]/td[2]/input[2]'))
    print("Login successfully!")


def send_email():
    driver_click((By.XPATH, '//*[@id="zb__NEW_MENU_title"]'))
    try:
        # 等待彈窗出現（如果需要）
        WebDriverWait(driver, 10).until(EC.alert_is_present())

        # 切換到彈窗
        alert = driver.switch_to.alert

        # 接受彈窗
        alert.accept()
    except TimeoutException:
        # 如果彈窗未出現，繼續執行其他操作
        pass
    driver_send_keys((By.XPATH, '//*[@id="zv__COMPOSE-1_to_control"]'), receiver)
    # for cc in carbon_copy:
    #     driver_send_keys((By.XPATH, '//*[@id="zv__COMPOSE-1_cc_control"]'), carbon_copy)
    new_title = utils.generate_title(name, title)
    driver_send_keys((By.XPATH, '//*[@id="zv__COMPOSE-2_subject_control"]'), new_title)
    driver_send_keys((By.XPATH, '//*[@id="ZmHtmlEditor2_body"]'), content)
    driver_click((By.XPATH, '//*[@id="zb__COMPOSE-1__SEND_title"]'))
    print("Email sent successfully!")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    login()
    send_email()