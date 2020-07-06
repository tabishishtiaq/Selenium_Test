from yayvo_test.test.test_pageobject.test_locators import locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class account_updating(object):

    def __init__(self, driver):

        self.driver = driver
        wait = WebDriverWait(driver, 10)
        self.message = wait.until(EC.element_to_be_clickable((By.XPATH, locators.notifi_message)))



