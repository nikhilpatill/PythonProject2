# utils/error_checker.py

from selenium.webdriver.common.by import By


class ErrorChecker:

    @staticmethod
    def check_visible_elements(elements):
        for element in elements:
            if element.is_displayed():
                return element
        return None

    @staticmethod
    def check_error_message(driver):
        xpath = (
            ".//div[@role='dialog']//p | "
            ".//div[contains(@style,'color: red')] | "
            ".//span[text()='Required'] | "
            ".//span[text()='Should be at least 5 characters'] | "
            ".//span[text()='Passwords do not match'] | "
            ".//span[text()='Invalid']"
        )
        elements = driver.find_elements(By.XPATH, xpath)
        visible_element = ErrorChecker.check_visible_elements(elements)

        if visible_element:
            msg_text = visible_element.text
            if msg_text and any(keyword in msg_text for keyword in [
                "Review", "Duplicate", "error", "mandatory", "Required",
                "Should be at least 5 characters", "Passwords do not match", "Invalid"
            ]):
                return msg_text
        return None
