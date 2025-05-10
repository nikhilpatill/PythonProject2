from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up Chrome options (optional)
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")  # Open browser in maximized mode

# Launch Chrome browser and open Google
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://pythonexamples.org/python-selenium-scroll-down/")
time.sleep(2)
driver.execute_script( "window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)


