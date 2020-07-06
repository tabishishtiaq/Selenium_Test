from yayvo_test.test.test_pageobject.test_locators import locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class My_Account(object):

    def __init__(self,driver):
        self.driver = driver
        wait = WebDriverWait(driver, 10)
        self.message = wait.until(EC.element_to_be_clickable((By.XPATH, locators.notifi_message)))


class account_button(object):

    def __init__(self,driver):
        self.driver = driver
        wait = WebDriverWait(driver,10)
        self.navigate = wait.until(EC.element_to_be_clickable((By.XPATH, locators.nav)))




