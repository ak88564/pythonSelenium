import logging
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# path=Service("/Users/kaditya/Downloads/chromedriver")
# from Pages.loginPage import LoginPage
from pageObjects.loginPage import LoginPage

#log = logging.getLogger(__name__)


class TestLogin:
    def test_OpenChrome(self):
        self.path=str("/Users/kaditya/Downloads/chromedriver")
        self.driver=webdriver.Chrome(executable_path=self.path)

        self.driver.get("https://www.amazon.in")
        mobile="8409478911"

        object1 = LoginPage(self.driver)
        object1.test_signin_section()
        object1.test_email_textbox(mobile)
        object1.test_email_submit()
        time.sleep(6)
        self.driver.close()
# driver.close()


# /Users/kaditya/Downloads