
import time
from Pageobjectmodel.loginpage import LoginPage
from selenium import webdriver



class Test_002_DDT_Login():
    baseURL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"


    def test_login_ddt(self):
        self.driver = webdriver.Chrome()  # Using Chrome WebDriver
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName("Admin")
        self.lp.setPassword("admin123")
        self.lp.clickLogin()



