from selenium.webdriver.common.by import By


class LoginPage:
    # Login Page
    textbox_username_id = "//input[@name='username']"
    textbox_password_id = "//input[@name='password']"
    button_login_xpath = "//button[@type='submit']"


    def __init__(self,driver):
        self.driver=driver

    def setUserName(self, username):
        self.driver.find_element(By.XPATH, "//input[@name='username']").send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
