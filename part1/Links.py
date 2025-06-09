import requests

from Utility.Baseutility import baseclass
from  selenium.webdriver.common.action_chains import ActionChains
from  selenium.webdriver.common.keys import Keys
from  selenium.webdriver.common.by import By
# Set up Chrome options (optional)
base = baseclass()
# Launch Chrome browser and open Google
driver = base.launch_browser("chrome")  # or base.setup(
driver.get('https://www.tutorialspoint.com/selenium/practice/links.php')

ele = driver.find_elements(By.TAG_NAME, 'a')

print(len(ele))

for link in ele:
     print(link.text)
count = 0

for link in ele :
     url = link.get_attribute(('href'))
     res =  requests.head(url)
     if res.status_code > 400:
        print(f"Link: {link.text} broken working")
        count += 1




