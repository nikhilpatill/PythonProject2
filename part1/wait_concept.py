import time
from telnetlib import EC

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from urllib3.util import wait_for_write
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utility.Baseutility import baseclass
from part1.alert_handle import alert_handle

# Set up Chrome options (optional)
base = baseclass()
# Launch Chrome browser and open Google
driver = base.launch_browser("chrome")  # or base.setup(
driver.get('https://www.tutorialspoint.com/selenium/practice/text-box.php')

wait = WebDriverWait(driver, 10)  # Wait for up to 10 seconds
name = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="fullname"]')))
name.send_keys("Hello World")
email = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="email"]')))
email.send_keys("nik12@gmail.com")
address = wait.until(EC.presence_of_element_located((By.XPATH, '//textarea[@placeholder="Currend Address"]')))
address.send_keys("India")
password = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="password"]')))
password.send_keys("nik123")
savebutoon = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@value="Submit"]')))
time.sleep(6)
savebutoon.click()
