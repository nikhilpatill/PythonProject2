

import time
from selenium import  webdriver

driver = webdriver.Edge()
#driver = webdriver.Firefox()
#driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
# Set up Chrome options (optional)

driver.get("https://www.google.com")
time.sleep(2)
driver.get("https://www.youtube.com/watch?v=ktDvVEEX55g&t=723s")
driver.back()
driver.forward()
driver.refresh()
