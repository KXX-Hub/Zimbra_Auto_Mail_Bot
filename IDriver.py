from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class IDriver():
    
    def driver_click(locator):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator)).click()