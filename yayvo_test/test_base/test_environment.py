import unittest
from selenium import webdriver
import datetime


class EnvironmentSetup(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= "/Users/tabish/Documents/Selenium_Test/venv/bin/chromedriver")
        print("Run Started at : " +str(datetime.datetime.now()))
        print("Chrome ENvironment Set up")
        print("========================================================================")
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()


    def tearDown(self):
        if (self.driver != None):
            print("========================================================================")
            print("Test Environment Destroyed")
            print("Run Completed  at : " + str(datetime.datetime.now()))
            self.driver.close()
            self.driver.quit()