import sys
import time
from datetime import date

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import utilities as utils

url = "https://mail.gss.com.tw/zimbra"
options = webdriver.ChromeOptions()
prefs = {'profile.default_content_setting_values': {'notifications': 2}}
options.add_experimental_option('prefs', prefs)
options.add_argument("--disable-infobars")
driver = webdriver.Chrome(options=options)
config = utils.read_config()
account = config.get('account')
password = config.get('password')
name = config.get('name')
receiver = config.get('receiver')
carbon_copy = config.get('carbon_copy').split("&")
title = config.get('title')
new_title = utils.generate_title(name, title)


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


def initialize_content():
    """Initialize the content."""
    print("Welcome to the Zimbra_Auto_Mail_Bot!")
    print("Please enter the content (use '&' to separate the content) ")
    content = input("Please enter the content : ")
    new_content = utils.generate_numbered_work_log(content)
    while True:
        confirm = input("Do you want to preview and confirm the email before sending? (Y/N): ").strip().upper()
        if confirm == "Y":
            print("Previewing the email:")
            print("Receiver: " + receiver)
            print("Carbon copy: " + str(carbon_copy))
            print("Title: " + new_title)
            print("Content: " + new_content)
            print("Date: " + str(date.today()))
            print("Name: " + name)

            confirm_send = input("Do you want to send the email? (Y/N): ").strip().upper()
            if confirm_send == "Y":
                login()
                send_email(new_content)
                break
            else:
                print("Email sending canceled.")
                print("Will be shut down in 10 seconds...")
                break
        elif confirm == "N":
            print("Email sending canceled.")
            print("Will be shut down in 10 seconds...")
            break
        else:
            print("Please enter 'Y' or 'N'.")


def login():
    driver.get(url)
    driver.maximize_window()
    driver_send_keys((By.XPATH, '//*[@id="username"]'), account)
    driver_send_keys((By.XPATH, '//*[@id="password"]'), password)
    driver_click((By.XPATH, '/html/body/div/div[1]/div[1]/form/table/tbody/tr[3]/td[2]/input[2]'))
    print("Login successfully!")


def send_email(new_content):
    driver_click((By.XPATH, '//*[@id="zb__NEW_MENU_title"]'))
    driver_send_keys((By.XPATH, '//*[@id="zv__COMPOSE-1_to_control"]'), receiver)
    driver.find_element(By.XPATH, '//*[@id="zv__COMPOSE-1_to_control"]').send_keys(Keys.ENTER)
    for cc in carbon_copy:
        driver_send_keys((By.XPATH, '//*[@id="zv__COMPOSE-1_cc_control"]'), cc)
        driver.find_element(By.XPATH, '//*[@id="zv__COMPOSE-1_cc_control"]').send_keys(Keys.ENTER)

    driver_send_keys((By.XPATH, '//*[@id="zv__COMPOSE-1_subject_control"]'), new_title)
    driver.find_element(By.XPATH, '//*[@id="zv__COMPOSE-1_subject_control"]').send_keys(Keys.ENTER)

    driver_send_keys((By.XPATH, '//*[@id="ZmHtmlEditor1_body"]'), new_content)
    driver_click((By.XPATH, '// *[ @ id = "zb__COMPOSE-1__SEND_MENU"] / table / tbody / tr'))
    print("Email sent successfully!")
    print("Receiver: " + receiver)
    print("Carbon copy: " + str(carbon_copy))
    print("Title: " + new_title)
    print("Content: " + new_content)
    print("Date: " + str(date.today()))
    print("Name: " + name)
    print("Will be shut down in 10 seconds...")
    time.sleep(10)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    initialize_content()

