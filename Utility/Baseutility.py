from selenium import  webdriver
import pytest
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

class baseclass:

    def __init__(self):
        self.driver = None

    def setup(self):
        options = Options()
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        return self.driver

    def launch_browser(self, browser_name):
        if browser_name.lower() == "chrome":
            options = Options()
            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                                           options=options)  # Fixed here
            self.driver.maximize_window()
            self.driver.implicitly_wait(5)
            return self.driver
        elif browser_name.lower() == "firefox":
            self.driver = webdriver.Firefox()
            self.driver.maximize_window()
            self.driver.implicitly_wait(5)
            return self.driver
        elif browser_name.lower() == "edge":
            self.driver = webdriver.Edge()
            self.driver.maximize_window()
            self.driver.implicitly_wait(5)
            return self.driver
        else:
            raise ValueError("Unsupported browser: {}".format(browser_name))

    def open_url(self, url):
        return self.driver.get(url)

    def close_browser(self):
        if self.driver:
            self.driver.quit()

    def new_Window_handle(self):
        currentwin = self.driver.current_window_handle
        for handle in self.driver.window_handles:
            if handle != currentwin:
                self.driver.switch_to.window(handle)
                self.driver.maximize_window()
                print("Switched to new window")
                break

    def current_window_handle(self):
        currentwin = self.driver.current_window_handle
        for handle in self.driver.window_handles:
            if handle == currentwin:
                self.driver.switch_to.window(currentwin)
                print("Switched to current window")
                break

    def switch_to_main_window(self):
        main_window = self.driver.window_handles[0]
        self.driver.switch_to.window(main_window)
        print("Switched to main window")


