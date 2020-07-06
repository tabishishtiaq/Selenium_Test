from yayvo_test.test.test_pageobject.test_locators import locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Home(object):

    def __init__(self, driver):
        self.driver = driver
        wait = WebDriverWait(driver, 10)
        self.email = wait.until(EC.element_to_be_clickable((By.NAME, locators.user_name)))
        self.pass_word = wait.until(EC.element_to_be_clickable((By.NAME, locators.password)))
        self.sign_in = wait.until(EC.element_to_be_clickable((By.NAME, locators.signin)))
