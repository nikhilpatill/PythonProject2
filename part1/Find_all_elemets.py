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

driver.get('https://rahulshettyacademy.com/AutomationPractice/')
# Wait for the page to load
# Wait for the presence of a specific element on t
my_input_text = driver.find_elements(By.XPATH, '//input[@type="radio"]')

for i in my_input_text:
    i.click()
    
ele = driver.find_element(By.XPATH, '//input[@id="autocomplete"]')
ele.click()
ele.send_keys('ind')
# Wait for the element to be clickable
option = driver.find_elements(By.XPATH, '//input[@type="checkbox"]')
option[0].click();
option[1].click();
option[2].click();


winbutton = driver.find_element(By.XPATH, '//button[@id="openwindow"]')
winbutton.click()

driver.current_window_handle

main_window = driver.current_window_handle
for handle in driver.window_handles:
    if handle != main_window:
        driver.switch_to.window(handle)
        break
    
    



