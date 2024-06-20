from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class UserManagement(BasePage):
    MAIN_TITLE = (By.CSS_SELECTOR, '.oxd-table-filter-title')
    ADD_USER_BUTTON = (By.CSS_SELECTOR, ".oxd-button-icon")
    ADD_USER_USER_ROLE_DROPDOWN = (By.CSS_SELECTOR, 'div:nth-child(1) > div > div:nth-child(1) > div > div:nth-child(2) > div > div')
    USER_ROLE_ADMIN_INPUT_VALUE = (By.CSS_SELECTOR, "div.oxd-select-dropdown.--positon-bottom > div:nth-child(2)")
    EMPLOYEE_INPUT_NAME = (By.CSS_SELECTOR, 'input[placeholder="Type for hints..."]')
    EMPLOYEE_NAME_FIRST_ITEM = (By.CSS_SELECTOR, 'div.oxd-autocomplete-dropdown.--positon-bottom > div:nth-child(1)')
    STATUS_DROPDOWN = (By.CSS_SELECTOR, 'div:nth-child(3) > div > div:nth-child(2) > div > div > div.oxd-select-text-input')
    STATUS_ENABLED = (By.CSS_SELECTOR, 'div:nth-child(2) > div > div.oxd-select-dropdown.--positon-bottom > div:nth-child(2)')
    USERNAME_INPUT = (By.CSS_SELECTOR, 'div:nth-child(4) > div > div:nth-child(2) > input')
    PASSWORD_INPUT = (By.CSS_SELECTOR, 'div.oxd-grid-item.oxd-grid-item--gutters.user-password-cell > div > div:nth-child(2) > input')
    CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, 'div.oxd-form-row.user-password-row > div > div:nth-child(2) > div > div:nth-child(2) > input')
    SAVE_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")


    def __init__(self, driver):
        super().__init__(driver)

    def main_title_text(self):
        return self.find_element(self.MAIN_TITLE).text
    
    def click_add_user(self):
        self.find_element(self.ADD_USER_BUTTON).click()

    def clik_user_role_dropdown(self):
        self.find_element(self.ADD_USER_USER_ROLE_DROPDOWN).click()

    def add_admin_input_value(self):
        self.find_element(self.USER_ROLE_ADMIN_INPUT_VALUE).click()
    
    def enter_employee_name(self, str):
        self.find_element(self.EMPLOYEE_INPUT_NAME).send_keys(str)

    def click_value_employee_name(self):
        self.find_element(self.EMPLOYEE_NAME_FIRST_ITEM).click()

    def click_status_dropdown(self):
        self.find_element(self.STATUS_DROPDOWN).click()

    def click_status_enabled(self):
        self.find_element(self.STATUS_ENABLED).click()

    def add_username(self, str):
        self.find_element(self.USERNAME_INPUT).send_keys(str)

    def enter_password(self, str):
        self.find_element(self.PASSWORD_INPUT).send_keys(str)
    
    def enter_confirm_password(self, str):
        self.find_element(self.CONFIRM_PASSWORD_INPUT).send_keys(str)
    
    def click_save(self):
        self.find_element(self.SAVE_BUTTON).click()


    


    
