from telnetlib import EC
from time import sleep

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from urllib3.util import wait_for_write

from Utility.Baseutility import baseclass

# Set up Chrome options (optional)
base = baseclass()
# Launch Chrome browser and open Google
driver = base.launch_browser("chrome")  # or base.setup(
driver.get('https://rahulshettyacademy.com/AutomationPractice/')


def switch_to_frame_for_tab():
    # Find all iframe elements on the page
    iframes = driver.find_elements(By.TAG_NAME, "iframe")  # corrected "ifram" to "iframe"
    total_frames = len(iframes)
    print(total_frames)
    for iframe in iframes:
        frame_id = iframe.get_attribute("name")
        print(frame_id)
        driver.switch_to.frame(iframe)


# Scroll down by 1000 pixels
driver.execute_script("window.scrollBy(0, 1500);")
base.switch_to_frame_for_tab()
ele = driver.find_element(By.XPATH, "(//a[text()='Courses'])[1]")
ele.click()
ele1 = driver.find_element(By.XPATH, "//h1[text()='Browse products']")
if ele1.is_displayed():
    print("Element is displayed")
    assert True
# Switch back to the default content

base.switch_back_mainframe_for_tab()
driver.execute_script("window.scrollTo(0, 0);")
option = driver.find_elements(By.XPATH, '//input[@type="checkbox"]')
option[0].click()
option[1].click()
option[2].click()
sleep(2)
