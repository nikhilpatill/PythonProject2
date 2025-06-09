from Utility.Baseutility import baseclass
from  selenium.webdriver.common.action_chains import ActionChains
from  selenium.webdriver.common.keys import Keys
# Set up Chrome options (optional)
base = baseclass()
# Launch Chrome browser and open Google
driver = base.launch_browser("chrome")  # or base.setup(
driver.get('https://www.tutorialspoint.com/selenium/practice/radio-button.php')

ele = driver.find_elements("xpath",'//input[@type="radio"]')

for i in range(len(ele)):
     ele[i].click()





