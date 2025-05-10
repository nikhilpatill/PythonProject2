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

initial_window_size = driver.get_window_size()
print('Initial window size :' + str(initial_window_size))

# Get initial window size
initial_window_size = driver.get_window_size()
print('Initial window size :' + str(initial_window_size))

# Get maximized window size
driver.maximize_window()
maximized_window_size = driver.get_window_size()
print('Maximized window size :' + str(maximized_window_size))

# Reset window size to its initial size
driver.set_window_size(initial_window_size['width'], initial_window_size['height'])

# Check if window is maximized
if initial_window_size == maximized_window_size:
    print('Window is in maximized state.')
else:
    print('Window is not in maximized state.')


