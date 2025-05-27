import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from part1.Baseutility import BaseUtility

BaseUtility = BaseUtility()
driver = BaseUtility.driver

BaseUtility.launch_browser("chrome", "https://www.youtube.com/watch?v=ktDvVEEX55g&t=723s")
my_input_text = driver.find_element(By.XPATH, '//input[@id="autocomplete"]')

# Enter a value in text field
my_input_text.send_keys("Apple")
# Take a screenshot after setting value
driver.save_screenshot("screenshot.png")

# Close the driver
driver.quit()
