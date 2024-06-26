from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
    
    def find_element(self, locator, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return element
        except TimeoutException:
            raise NoSuchElementException(f"Element not found: {locator}") 
    
    def find_elements(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(locator))
    
    def wait_for_text_change(self, locator, text):
        return WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(locator, text))
    
    def go_to(self, url):
        self.driver.get(url)

