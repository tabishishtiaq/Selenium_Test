from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from yayvo_test.test.test_pageobject.test_locators import locators


class sub_account(object):
    def __init__(self, driver):
        self.driver = driver
        wait = WebDriverWait(driver, 10)
        self.wish = wait.until(EC.element_to_be_clickable((By.XPATH, locators.mywish)))


class checkout(object):
    def __init__(self,driver):
        self.driver = driver
        wait = WebDriverWait(driver,10)
        self.check = wait.until(EC.element_to_be_clickable((By.XPATH,locators.check_out)))

class click(object):
    def __init__(self,driver):
        self.driver = driver
        wait = WebDriverWait(driver,10)
        self.click = wait.until(EC.element_to_be_clickable((By.XPATH,locators.click_here)))

class account_information(object):
    def __init__(self,driver):
        self.driver = driver
        wait =WebDriverWait(driver,10)
        self.acc_info = wait.until(EC.element_to_be_clickable((By.XPATH,locators.acc_info)))


class form_info(object):
    def __init__(self,driver):
        self.driver = driver
        wait = WebDriverWait(driver,10)
        self.first_name = wait.until(EC.element_to_be_clickable((By.XPATH,locators.first_name)))
        self.last_name = wait.until(EC.element_to_be_clickable((By.XPATH, locators.last_name)))
        self.email_add = wait.until(EC.element_to_be_clickable((By.XPATH, locators.email)))
        self.cntct_number = wait.until(EC.element_to_be_clickable((By.XPATH, locators.cont_nmbr)))
        self.cnic = wait.until(EC.element_to_be_clickable((By.XPATH, locators.cnic)))
        self.save_btn = wait.until(EC.element_to_be_clickable((By.XPATH, locators.save)))


