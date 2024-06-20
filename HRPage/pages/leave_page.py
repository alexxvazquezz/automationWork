from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LeavePage(BasePage):
    MAIN_TITLE = (By.CSS_SELECTOR, '.orangehrm-main-title')
    LEAVE_LIST_FILTER_TITLE = (By.CSS_SELECTOR, '.oxd-table-filter-title')

    def __init__(self, driver):
        super().__init__(driver)

    def main_title_text(self):
        return self.find_element(self.MAIN_TITLE).text
    
    def leave_list_title(self):
        return self.find_element(self.LEAVE_LIST_FILTER_TITLE).text
    
