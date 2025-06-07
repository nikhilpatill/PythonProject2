import logging
import time
from stat import filemode
import self
from pages.loginpage import LoginPage
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from Utility.Baseutility import baseclass
from Utility.CustomLogger import LogGenerator
from Utility import XLUtils
import allure


class Test_002_DDT_Login:
    baseURL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    path = ".//TestData/LoginData.xlsx"

    logger = LogGenerator.loggen()

    def test_login_ddt1(self):
        self.logger.info("********** Verifying Login Test **********")
        self.logger.info("********** Verifying Login Test **********")
        self.driver = baseclass.launch_browser(self, "firefox")
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
            self.driver.save_screenshot(".\\Screenshot\\" + "test_login_ddt1.png")
            self.logger.info("********** Login Test Passed **********")
        else:
            print("Login failed")
            assert False
            self.driver.save_screenshot(".\\Screenshot\\" + "test_login_ddt1.png")
            self.logger.info("********** Login Test Failed **********")
        self.driver.close()


    def test_login_error(self):
        self.logger.info("********** Verifying Login Test **********")
        self.logger.info("********** Verifying Login Test **********")
        self.driver = baseclass.launch_browser(self, "chrome")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.driver.implicitly_wait(10)
        self.lp.setUserName("Admin")
        self.lp.clickLogin()
        error_msg = self.lp.get_error_message()
        assert error_msg == "Required"
        assert True
        self.logger.info("********** Login Test Passed **********")
        print("Error:", error_msg)
        #self.logger.info("Error:", error_msg)
        self.driver.close()


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
            self.driver.save_screenshot(".\\Screenshot\\" + "test_login_ddt1.png")
