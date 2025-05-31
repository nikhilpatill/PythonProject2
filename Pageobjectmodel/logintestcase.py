
import time

import self
from pages.loginpage import LoginPage
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from Utility.Baseutility import baseclass


class Test_002_DDT_Login :
    baseURL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    def test_login_ddt1(self):
        self.driver= baseclass.setup(self)
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.driver.implicitly_wait(10)
        self.lp.setUserName("Admin")
        self.lp.setPassword("admin123")
        self.lp.clickLogin()
        actual_title = self.lp.getLoginTitle()
        if actual_title == "OrangeHRM":
            print("Login successful")
            assert True
        else:
            print("Login failed")
            assert False

    def test_login_ddt(self):
        options = Options()
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.driver.implicitly_wait(10)
        self.lp.setUserName("Admin")
        self.lp.setPassword("admin123")
        self.lp.clickLogin()
        actual_title = self.lp.getLoginTitle()
        if actual_title == "OrangeHRM":
            print("Login successful")
            assert True
        else :
            print("Login failed")
            assert False





