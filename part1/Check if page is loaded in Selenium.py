from telnetlib import EC

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up Chrome options (optional)
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")  # Open browser in maximized mode

# Launch Chrome browser and open Google
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get('https://pythonexamples.org/tmp/selenium/index-13.html')

# Set the maximum amount of time to wait for the page to load (in seconds)
timeout = 10

# Wait for the presence of a specific element on the page
try:
    element_present = EC.presence_of_element_located((By.XPATH, "//*[@id='child3']"))
    WebDriverWait(driver, timeout).until(element_present)
    print("Page loaded successfully!")
except TimeoutException:
    print("Timed out waiting for page to load.")

# Close the driver
driver.quit()