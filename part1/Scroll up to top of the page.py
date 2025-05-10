from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up Chrome options (optional)
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")  # Open browser in maximized mode

# Launch Chrome browser and open Google
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Navigate to the url
driver.get('https://rahulshettyacademy.com/AutomationPractice')

# Find first input text field
my_input_text = driver.find_element(By.XPATH, '//input[@id="autocomplete"]')

# Enter a value in text field
my_input_text.send_keys("Apple")

# Take a screenshot after setting value
driver.save_screenshot("screenshot.png")

driver.execute_script("window.scrollTo(0, 0);")

# Close the driver
driver.quit()
