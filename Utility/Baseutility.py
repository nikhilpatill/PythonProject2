from selenium import  webdriver
import pytest
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

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

    def alert_handle(self):
        alert = self.driver.switch_to.alert
        alert.accept()

    def aler_dismiss(self):
        alert = self.driver.switch_to.alert
        alert.dismiss()

    def aler_input(self):
        alert = self.driver.switch_to.alert
        alert.send_keys("Hello")

    def switch_to_frame_for_tab(self):
        # Find all iframe elements on the page
        iframes = self.driver.find_elements(By.TAG_NAME, "iframe")  # corrected "ifram" to "iframe"
        total_frames = len(iframes)
        print(total_frames)
        for iframe in iframes:
            frame_id = iframe.get_attribute("name")
            print(frame_id)
            self.driver.switch_to.frame(iframe)

    def switch_back_mainframe_for_tab(self):
        # Switch back to the main content from the iframe
        self.driver.switch_to.default_content()
        print("Switched back to main content")
