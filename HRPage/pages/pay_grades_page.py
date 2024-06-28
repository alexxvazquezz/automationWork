from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class PayGrades(BasePage):
    MAIN_HEADER = (By.CSS_SELECTOR, 'div.orangehrm-header-container > h6')

    def __init__(self, driver):
        super().__init__(driver)

    def main_header_text(self):
        text = self.find_element(self.MAIN_HEADER).text
        return text
    