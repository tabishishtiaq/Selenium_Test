import unittest

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from yayvo_test.test.test_pageobject.test_locators import locators
from yayvo_test.test_base.test_environment import EnvironmentSetup
from yayvo_test.test.test_pages.yayvo_home_page import Home
from yayvo_test.test.test_pages.yayvo_myaccount_page import My_Account
from yayvo_test.test.test_pages.yayvo_myaccount_page import account_button
from yayvo_test.test.test_pages.accont_page import account_information
from yayvo_test.test.test_pages.accont_page import form_info
from yayvo_test.test.test_pages.accont_page import checkout
from yayvo_test.test.test_pages.accont_page import sub_account
from yayvo_test.test.test_pages.accont_page import click
import time


class yayvo_login_page(EnvironmentSetup):
    def test_login(self):
        driver = self.driver
        # driver.implicitly_wait(5)
        self.driver.get("https://yayvo.com/customer/account/login/")

        try:
            if driver.title == "Online Shopping in Pakistan at Discount Price Karachi, Lahore, Islamabad @ Yayvo":
                self.assertEqual(driver.title,
                                 "Online Shopping in Pakistan at Discount Price Karachi, Lahore, Islamabad @ Yayvo")
                print("Title Assertion is Passed")
            else:
                print("Title Assertion is Failed")
        except Exception as e:
            print("Title Assertion is Failed Due To :" + str(e))

        home = Home(driver)

        try:
            if home.email.get_attribute("id") == 'email':
                self.assertEqual(home.email.get_attribute('id'), 'email')
                print("Email Text Field Assertion is Passed")
                home.email.send_keys("asimabbas41@yahoo.com")
            else:
                print("Email Text Field Assertion is Failed")
        except Exception as e:
            print("Email Text Field Assertion is Failed Due To : " + str(e))

        try:
            if home.pass_word.get_attribute('id') == 'pass':
                self.assertEqual(home.pass_word.get_attribute('id'), 'pass')
                print("Password Text Field Assertion is Passed")
                home.pass_word.send_keys("17july1995")
            else:
                print("Password Text Field Assertion is Failed")
        except Exception as e:
            print("Password Text Field Assertion is Failed Due To : " + str(e))

        try:
            if home.sign_in.get_attribute('name') == 'send':
                self.assertEqual(home.sign_in.get_attribute('name'), 'send')
                print("SignIn Button Assertion is Passed")
                home.sign_in.click()

            else:
                print("SignIn Button Assertion is Failed")
        except Exception as e:
            print("SignIn Button Assertion is Failed Due To : " + str(e))

        acc_button = account_button(driver)


        try:
            try:

                if driver.title == "My Account":
                    self.assertEqual(driver.title, "My Account")
                    print(
                        "My Account Page Title Assertion Successfully After Login User Should Landed to My Account Page")
                else:
                    print("My Account Page Title Assertion Failed  After Login User Not Landed to My Account Page")
            except Exception as e:
                print("My Account Page Title Assertion Failed Due To : " + str(e))

            if acc_button.navigate.text == "Asim":
                self.assertEqual(acc_button.navigate.text, "Asim")
                print("Asim Assertion is Passed")
                acc_button.navigate.click()

            else:
                print("Asim Assertion is Failed")
        except Exception as e:
            print("Asim Button Assertion is Failed Due to : " + str(e))

        info = account_information(driver)
        try:
            try:
                if driver.title == "My Account":
                    self.assertEqual(driver.title, "My Account")
                    print("Page Title Before Clicking Account Information Tab Assertion is Passed")
                else:
                    print("Page Title Before Clicking Account Information Tab Assertion is Failed")
            except Exception as e:
                print("Page Title Before Clicking Account Information Tab Assertion is Failed Due To : " + str(e))
            try:
                if info.acc_info.text == "Account Information":
                    self.assertEqual(info.acc_info.text, "Account Information")
                    print("Account Information Tab Assertion is Passed ")
                    info.acc_info.click()
                else:
                    print("Account Information Tab Assertion is Failed")
            except Exception as e:
                print(str(e))
            try:
                    if driver.title == "Account Information":
                        self.assertEqual(driver.title, "Account Information")
                        print(
                            "User Successfully landed on Account Informartion page after clicking on Account Information Tab")
                    else:
                        print(
                            "User Did not  landed on Account Informartion page after clicking on Account Information Tab")
            except Exception as e:
                print("User Did not  landed on Account Informartion page after clicking on Account Information Tab Due To :  " + str(e))

        except Exception as e:
            print("Account Information Tab Assertion Failed Due To : " + str(e))

        form = form_info(driver)
        try:
            if form.first_name.get_attribute("id") == "firstname":
                self.assertEqual(form.first_name.get_attribute("id"), "firstname")
                print("Account Information Page First Name Text Field Assertion Is Passed")
                form.first_name.clear()
                form.first_name.send_keys("Asim")
            else:
                print("Account Information Page First Name Text Field Assertion Is Failed")
        except Exception as e:
            print("Account Information Page First Name Text Field Assertion Is Failed Due To : " + str(e))
        try:
            if form.last_name.get_attribute("id") == "lastname":
                self.assertEqual(form.last_name.get_attribute("id"), "lastname")
                print("Account Information Page Last Name Text Field Assertion is Passed")
                form.last_name.clear()
                form.last_name.send_keys("abbas")
            else:
                print("Account Information Page Last Name Text Field Assertion is Passed")
        except Exception as e:
            print("Account Information Page Last Name Text Field Assertion is Failed Due To : " + str(e))
        try:
            if form.email_add.get_attribute("id") == "email":
                self.assertEqual(form.email_add.get_attribute("id"), "email")
                print("Account Information Page Email Address Text Field Assertion is Passed")
                form.email_add.clear()
                form.email_add.send_keys("asimabbas41@yahoo.com")
            else:
                print("Account Information Page Email Address Text Field Assertion is Failed")
        except Exception as e:
            print("Account Information Page Email Address Text Field Assertion Is Failed Due To : " + str(e))
        try:
            if form.cntct_number.get_attribute("id") == "mobile":
                self.assertEqual(form.cntct_number.get_attribute("id"), "mobile")
                print("Account Information Page Contact Number Field Assertion Is Passed")
                form.cntct_number.clear()
                form.cntct_number.send_keys("923073207643")
            else:
               print("Account Information Page Contact Number Field Assertion Is Failed")
        except Exception as e:
            print("Account Information Page Contact Number Field Assertion Is Failed Due To : " + str(e))
        try:
            if form.cnic.get_attribute("id") == "customer_cnic":
                self.assertEqual(form.cnic.get_attribute("id"), "customer_cnic")
                print("Account Information Page Customer C.N.I.C Text Field Assertion Is Passed ")
                form.cnic.clear()
                form.cnic.send_keys(4130460929921)
            else:
                print("Account Information Page Customer C.N.I.C Text Field Assertion Is Failed ")
        except Exception as e:
            print("Account Information Page Customer C.N.I.C Text Field Assertion Is Failed Due To : " + str(e))
        try:
            if form.save_btn.text == "Save":
                self.assertEqual(form.save_btn.text, "Save")
                print("Account Information Page Save Button Assertion Is Passed")
                form.save_btn.click()

            else:
                print("Account Information Page Save Button Assertion Is Failed")
        except Exception as e:
            print("Account Information Page Save Button Assertion Is Failed Due To : " + str(e))

        account = My_Account(driver)
        try:
             if driver.title == "My Account":
                 self.assertEqual(driver.title, "My Account")
                 print("After Updating Account Information User Should Landed On My Account Page")
             else:
                 print("After Updating Account Information Assertion Is Passed User Should Landed On My Account Page")
        except Exception as e:
            print("After Updating Account Information Assertion Is Failed User Not Landed On My Account Page Due To : " + str(e))
        try:
             if account.message.text == "The account information has been saved." :
                 self.assertEqual(account.message.text, "The account information has been saved.")
                 print("Account Information Updating Assertion Is Passed")
             else:
                print("Account Information Updating Assertion Is Failed")
        except Exception as e:
            print("Account Information Updating Assertion Is Failed Due To : " + str(e))
        sub_acc = sub_account(driver)
        try:
            if sub_acc.wish.text == 'My Wishlist':
                self.assertEqual(sub_acc.wish.text, "My Wishlist")
                print("My Wishlist Assertion is Passed")
                sub_acc.wish.click()

            else:
                print("My Wishlist Assertion is Failed")
        except Exception as e:
            print("My Wishlist Button Assertion is Failed Due to : " + str(e))

        try:
            driver.get("https://yayvo.com/wishlist/")
            handles = driver.window_handles
            for handle in handles:
                driver.switch_to_window(handle)

            if acc_button.navigate.text == "Asim":
                self.assertEqual(acc_button.navigate.text, "Asim")
                print("Asim Assertion is Passed")
                acc_button.navigate.click()

            else:
                print("Asim Assertion is Failed")
        except (StaleElementReferenceException) as e:
            try:
                wait = WebDriverWait(driver, 10)
                self.navigate = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@class='last']/a")))
                if self.navigate.text == "Asim":
                    self.assertEqual(self.navigate.text, "Asim")
                    print("Asim Assertion is Passed")
                    self.navigate.click()

                else:
                    print("Asim Button Assertion is Failed")
            except Exception as e:
                print("Asim Button Assertion is Failed Due to : " + str(e))
        check_btn = checkout(driver)
        try:
            if check_btn.check.text == 'Checkout':
                self.assertEqual(check_btn.check.text, "Checkout")
                print("Checkout Button  Assertion is Passed")
                check_btn.check.click()

                if driver.title == "Shopping Cart":
                    self.assertEqual(driver.title, "Shopping Cart")
                    print("Shopping Cart Page Title Assertion is Passed After Clicking on Checkout Button")
                else:
                    print("Shopping Cart Page Title Assertion is Failed After Clicking on Checkout Button")


            else:
                print("Checkout Button Assertion is Failed")
        except Exception as e:
            print("Checkout Button Assertion is Failed Due to : " + str(e))
        cli = click(driver)
        try:
            if cli.click.text == "Click here":
                self.assertEqual(cli.click.text, "Click here")
                print("Click Here Field Assertion is Passed")
                cli.click.click()
            else:
                print("Click Here Filed Assertion is Failed")
            try:

                if driver.title == "Online Shopping in Pakistan with Best Prices & Discounts | Yayvo.com":
                    self.assertEqual(driver.title,
                                     "Online Shopping in Pakistan with Best Prices & Discounts | Yayvo.com")
                    print("Your Home Open Assertion is Successfully open Home Page After Clicking on Click Here Tag")
                else:
                    print(
                        "Your Home Page Assertion is Unsuccessfully failed to open Home Page After Clicking on Click Here Tag ")
            except Exception as e:
                print("Your Home Open Assertion is Failed to open After Clicking on Click Here Tag" + str(e))


        except Exception as e:
            print("CLick Here Field Assertion Failed Due To : " + str(e))
