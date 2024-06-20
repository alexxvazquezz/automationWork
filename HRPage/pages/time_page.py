from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class TimePage(BasePage):
    MAIN_TITLE = (By.CSS_SELECTOR, '.orangehrm-main-title')

    def __init__(self, driver):
        super().__init__(driver)

    def main_title_text(self):
        return self.find_element(self.MAIN_TITLE).text
    
