from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import HtmlTestRunner
import time
import sys

sys.path.append("B:\\SQA Preparation\\Unit Testing\\Page Object Model")
from pageObjects.login_page import LoginTest


class Test_Login(unittest.TestCase):
    base_url = "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    email = "admin@yourstore.com"
    passwords = "admin"
    driver = webdriver.Chrome(ChromeDriverManager().install())

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.base_url)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    def test_login(self):
        lp = LoginTest(self.driver)  # Creating an object
        lp.set_email(self.email)
        lp.set_password(self.passwords)
        lp.click_login()
        time.sleep(5)
        self.assertEqual("Dashboard / nopCommerce administration", self.driver.title)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="B:\\SQA Preparation\\Unit Testing\\Page Object Model\\Reports"))
