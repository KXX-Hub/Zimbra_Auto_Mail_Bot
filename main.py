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


def initialize_content_and_send_email():
    """Initialize the content."""
    print("Welcome to the Zimbra_Auto_Mail_Bot!")
    print("Please enter the content (use '&' to separate the content) ")
    content = input("Please enter the content : ")
    new_content = utils.generate_numbered_work_log(content)
    is_confirm = False
    confirm_send = ""
    while True:
        if not is_confirm:
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
        elif confirm_send == "N":
            content = input("Please enter the content : ")
            new_content = utils.generate_numbered_work_log(content)
            continue
        else:
            is_confirm = True
            confirm_send = input("Please enter 'Y' or 'N':").strip().upper()


def login():
    driver.get(url)
    driver.maximize_window()
    driver_send_keys((By.XPATH, '//*[@id="username"]'), account)
    driver_send_keys((By.XPATH, '//*[@id="password"]'), password)
    driver_click((By.XPATH, '/html/body/div/div[1]/div[1]/form/table/tbody/tr[3]/td[2]/input[2]'))
    print("Login successfully!")


def bot_send_email(new_content, compose_version):
    # Enter the receiver's email address
    driver_send_keys((By.XPATH, f'//*[@id="zv__COMPOSE-{compose_version}_to_control"]'), receiver)
    driver.find_element(By.XPATH, f'//*[@id="zv__COMPOSE-{compose_version}_to_control"]').send_keys(Keys.ENTER)

    # Enter carbon copy (cc) email addresses
    for cc in carbon_copy:
        driver_send_keys((By.XPATH, f'//*[@id="zv__COMPOSE-{compose_version}_cc_control"]'), cc)
        driver.find_element(By.XPATH, f'//*[@id="zv__COMPOSE-{compose_version}_cc_control"]').send_keys(Keys.ENTER)

    driver_send_keys((By.XPATH, f'//*[@id="zv__COMPOSE-{compose_version}_subject_control"]'), new_title)
    driver.find_element(By.XPATH, f'//*[@id="zv__COMPOSE-{compose_version}_subject_control"]').send_keys(Keys.ENTER)

    driver_send_keys((By.XPATH, f'//*[@id="ZmHtmlEditor{compose_version}_body"]'), new_content)
    driver_click((By.XPATH, f'// *[ @ id = "zb__COMPOSE-{compose_version}__SEND_MENU"] / table / tbody / tr'))


def determine_compose_version():
    for compose_version in range(1,10000):
        # Check if the "Send" button is present
        current_compose_version = driver.find_elements(By.XPATH, f'//*[@id="zv__COMPOSE-{compose_version}_to_control"]')

        if current_compose_version:
            return compose_version


def send_email(new_content):
    driver_click((By.XPATH, '//*[@id="zb__NEW_MENU_title"]'))
    compose_version = int(determine_compose_version())
    bot_send_email(new_content, compose_version)
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
    initialize_content_and_send_email()
