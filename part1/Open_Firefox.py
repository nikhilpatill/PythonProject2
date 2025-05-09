from selenium import webdriver
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
import time
# Initialize Firefox driver instance
driver = webdriver.Firefox(service=FirefoxService(executable_path=GeckoDriverManager().install()))

driver.get("https://www.google.com")
time.sleep(2)
driver.get("https://www.youtube.com/watch?v=ktDvVEEX55g&t=723s")
driver.back()
driver.forward()
driver.refresh()


