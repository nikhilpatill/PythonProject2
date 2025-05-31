from time import sleep

from selenium.webdriver.common.by import By
from time import sleep


class LoginPage:
    # Login Page
    textbox_username_id = "//input[@name='username']"
    textbox_password_id = "//input[@name='password']"
    button_login_xpath = "//button[@type='submit']"



    def __init__(self,driver):

        self.driver=driver

    def setUserName(self, username):
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, "//input[@name='username']").send_keys(username)
        self.driver.implicitly_wait(10)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(password)
    def clickLogin(self):
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        sleep(2)
    def getLoginTitle(self):
        return self.driver.title