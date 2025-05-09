from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up Chrome options (optional)
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")  # Open browser in maximized mode

# Launch Chrome browser and open Google
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.google.com")

my_current_url = driver.current_url
print(my_current_url)

my_title = driver.title
print(my_title)
# Close the browser
driver.quit()
