from Utility.Baseutility import baseclass
from  selenium.webdriver.common.action_chains import ActionChains
from  selenium.webdriver.common.keys import Keys
# Set up Chrome options (optional)
base = baseclass()
# Launch Chrome browser and open Google
driver = base.launch_browser("chrome")  # or base.setup(
driver.get('https://www.tutorialspoint.com/selenium/practice/buttons.php')


def actionclick(ele):
    action = ActionChains(driver)
    action.click().perform()
def actiondbclick(ele):
    action = ActionChains(driver)
    action.double_click().perform()
def actionrightclick(ele):
    action = ActionChains(driver)
    action.context_click().perform()
def actionsendkeys(ele, text):
    action = ActionChains(driver)
    action.send_keys_to_element(ele, text).perform()
def actionkeysenter():
    action = ActionChains(driver)
    action.send_keys_to_element(Keys.ENTER).perform()

button = driver.find_element("xpath", '//button[text()="Click Me"]')
action = ActionChains(driver)
base.actionclick(button)
text = driver.find_element("xpath", '//div[@id="welcomeDiv"]')
text.is_enabled()
base.actionkeysTab(text)

dbclickbutton = driver.find_element("xpath", '//button[text()="Double Click Me"]')
base.actiondbclick(dbclickbutton)

rightclickbuton = driver.find_element("xpath", '//button[text()="Right Click Me"]')
base.actionrightclick(rightclickbuton)

driver.get("https://www.tutorialspoint.com/selenium/practice/text-box.php")

name = driver.find_element("xpath", '//input[@id="fullname"]')
base.actionsendkeys(name, "Hello World")
base.actionkeysTab(name)

email = driver.find_element("xpath", '//input[@id="email"]')
base.actionsendkeys(email, "nikhil12@gmail.com")
base.actionkeysTab(email)

address = driver.find_element("xpath", '//textarea[@placeholder="Currend Address"]')
base.actionsendkeys(address, "pune mumbai")
base.actionkeysTab(address)
password = driver.find_element("xpath", '//input[@id="password"]')
base.actionsendkeys(address, "success@123")
base.actionkeysTab(password)
save = driver.find_element("xpath", '//input[@value="Submit"]')
base.actionclick(save)








