from selenium import  webdriver
import pytest
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

class baseclass:

    def setup(self):
        options = Options()
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.maximize_window()
        driver.implicitly_wait(5)
        return driver

    def launch_browser(self, browser_name, url):
        if browser_name.lower() == "chrome":
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.implicitly_wait(5)
            self.driver.get(url)
            return self.driver
        elif browser_name.lower() == "firefox":
            self.driver = webdriver.Firefox()
            self.driver.get(url)
            self.driver.maximize_window()
            self.driver.implicitly_wait(5)
            return self.driver
        elif browser_name.lower() == "edge":
            self.driver = webdriver.Edge()
            self.driver.get(url)
            self.driver.maximize_window()
            self.driver.implicitly_wait(5)
            return self.driver
        else:
            raise ValueError("Unsupported browser: {}".format(browser_name))




    def open_url(self, url):
        self.driver.get(url)

    def close_browser(self):
        if self.driver:
            self.driver.quit()

