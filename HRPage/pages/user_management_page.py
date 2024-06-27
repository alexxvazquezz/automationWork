from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

class UserManagement(BasePage):
    MAIN_TITLE = (By.CSS_SELECTOR, '.oxd-table-filter-title')
    ADD_USER_BUTTON = (By.CSS_SELECTOR, ".oxd-button-icon")
    ADD_USER_USER_ROLE_DROPDOWN = (By.CSS_SELECTOR, 'div:nth-child(1) > div > div:nth-child(1) > div > div:nth-child(2) > div > div')
    USER_ROLE_ADMIN_INPUT_VALUE = (By.CSS_SELECTOR, "div.oxd-select-dropdown.--positon-bottom > div:nth-child(2)")
    EMPLOYEE_INPUT_NAME = (By.CSS_SELECTOR, 'div:nth-child(1) > div > div:nth-child(2) > div > div:nth-child(2) > div > div > input')
    EMPLOYEE_NAME_FIRST_ITEM_ADD = (By.CSS_SELECTOR, 'div.oxd-autocomplete-dropdown.--positon-bottom > div.oxd-autocomplete-option.--selected')
    STATUS_DROPDOWN = (By.CSS_SELECTOR, 'div:nth-child(3) > div > div:nth-child(2) > div > div > div.oxd-select-text-input')
    STATUS_ENABLED = (By.CSS_SELECTOR, 'div:nth-child(2) > div > div.oxd-select-dropdown.--positon-bottom > div:nth-child(2)')
    USERNAME_INPUT = (By.CSS_SELECTOR, 'div:nth-child(4) > div > div:nth-child(2) > input')
    PASSWORD_INPUT = (By.CSS_SELECTOR, 'div.oxd-grid-item.oxd-grid-item--gutters.user-password-cell > div > div:nth-child(2) > input')
    CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, 'div.oxd-form-row.user-password-row > div > div:nth-child(2) > div > div:nth-child(2) > input')
    SAVE_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    REQUIRED_ERROR_ALL = "form > div:nth-child(1) > div > div:nth-child({}) > div > span"
    PASSWORD_ERROR = (By.CSS_SELECTOR, 'div.oxd-grid-item.oxd-grid-item--gutters.user-password-cell > div > span')
    SHOULD_BE_5_CHARACTERS = (By.CSS_SELECTOR,'form > div:nth-child(1) > div > div:nth-child(4) > div > span')
    PASSWORDS_DO_NOT_MATCH = (By.CSS_SELECTOR, 'form > div.oxd-form-row.user-password-row > div > div:nth-child(2) > div > span')
    PASSWORD_STRENGTH_LABEL = (By.CSS_SELECTOR, 'div.oxd-grid-item.oxd-grid-item--gutters.user-password-cell > span')
    CANCEL_BUTTON = (By.CSS_SELECTOR, 'button.oxd-button.oxd-button--medium.oxd-button--ghost')
    ALREADY_EXISTS = (By.CSS_SELECTOR, 'div:nth-child(1) > div > div:nth-child(4) > div > span')
    SEARCH_INPUT_USERNAME = (By.CSS_SELECTOR, 'div:nth-child(2) > input')
    USER_IN_TABLE = (By.CSS_SELECTOR, 'div.oxd-table-body > div.oxd-table-card')
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'button.oxd-button.oxd-button--medium.oxd-button--secondary.orangehrm-left-space')
    USER_ROLE_DROPDOWN = (By.CSS_SELECTOR, 'div:nth-child(2) > div > div:nth-child(2) > div > div > div.oxd-select-text-input')
    FIRST_ELEMENT_USER_TABLE = (By.CSS_SELECTOR, 'div.oxd-table-body > div:nth-child(2) > div > div:nth-child(4) > div')
    SEARCH_INPUT_EMPLOYEE_NAME = (By.CSS_SELECTOR, 'div > div:nth-child(2) > div > div > input')
    EMPLOYEE_NAME_DROPDOWN = (By.CSS_SELECTOR, 'div.oxd-autocomplete-dropdown.--positon-bottom > div > span')


    def __init__(self, driver):
        super().__init__(driver)

    def main_title_text(self):
        return self.find_element(self.MAIN_TITLE).text
    
    def click_add_user(self):
        self.find_element(self.ADD_USER_BUTTON).click()

    def click_user_role_dropdown(self):
        self.find_element(self.ADD_USER_USER_ROLE_DROPDOWN).click()

    def add_admin_input_value(self):
        self.find_element(self.USER_ROLE_ADMIN_INPUT_VALUE).click()
    
    def enter_employee_name(self, str):
        self.find_element(self.EMPLOYEE_INPUT_NAME).send_keys(str)

    def click_value_employee_name(self):
       element = self.find_element(self.EMPLOYEE_NAME_FIRST_ITEM_ADD)
       element.click

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
    
    def submit_user_form(self):
        self.find_element(self.SAVE_BUTTON).click()

    def add_new_user(self, employeeName, userName, password):
        self.click_add_user()
        self.click_user_role_dropdown()
        self.add_admin_input_value()
        self.enter_employee_name(employeeName)
        time.sleep(2)
        self.click_status_dropdown()
        self.click_status_enabled()
        self.add_username(userName)
        self.enter_password(password)
        self.enter_confirm_password(password)

    def validate_username_in_table(self, username):
        i = 1
        while True:
            nth_child_selector = f"div.oxd-table-body > div:nth-child({i}) > div > div:nth-child(2) > div"
            try:
                username_element = self.find_element((By.CSS_SELECTOR, nth_child_selector))
                if username_element.text == username:
                    return True
            except NoSuchElementException:
                break

            i += 1

        return False
    
    def find_first_non_admin_username(self):
        i = 1
        while True:
            nth_child_selector = f"div.oxd-table-body > div:nth-child({i}) > div > div:nth-child(2) > div"

            try:
                username_element = self.find_element((By.CSS_SELECTOR, nth_child_selector))
                username = username_element.text.strip()
                if username != 'Admin':
                    return username
            except NoSuchElementException:
                break
            i += 1
        return None
    
    def click_cancel(self):
        self.find_element(self.CANCEL_BUTTON).click()

    def validate_required_all_fields(self):
        for i in range(1, 5):
            element_locator = self.REQUIRED_ERROR_ALL.format(i)
            try:
                element = self.find_element((By.CSS_SELECTOR, element_locator))
                if 'required' not in element.text.lower():
                    return False
            except:
                return False
        return True

    def validate_user_role(self, user_role):
        i = 1
        while True:
            try:
                element = self.find_element((By.CSS_SELECTOR, f'div.oxd-table-body > div:nth-child({i}) > div > div:nth-child(3) > div'))
                text = element.text.strip()
                if text != user_role:
                    return False
            except NoSuchElementException:
                break
            i += 1
        return True
    

    def validate_employee_name(self, employee_name):
        i = 1
        while True:
            try:
                element = self.find_element((By.CSS_SELECTOR, f'div.oxd-table-body > div:nth-child({i}) > div > div:nth-child(4) > div'))
                text = element.text.strip()
                if text != employee_name:
                    return False
            except NoSuchElementException:
                break
            i += 1
        return True


    def validate_password_error(self):
        return self.find_element(self.PASSWORD_ERROR).text
    
    def validate_should_be_at_least_5_characters_username(self):
        return self.find_element(self.SHOULD_BE_5_CHARACTERS).text
    
    def validate_passwords_do_not_match(self):
        return self.find_element(self.PASSWORDS_DO_NOT_MATCH).text
    
    def wait_password_strength_label_text(self, text):
        text_value = self.wait_for_text_change(self.PASSWORD_STRENGTH_LABEL, text)
        return text_value
    
    def clear_password_field(self):
        password_input = self.find_element(self.PASSWORD_INPUT)
        password_input.clear()

    def validate_already_exists_error(self, text):
        return self.wait_for_text_change(self.ALREADY_EXISTS, text)
    
    def enter_username_search(self, str):
        self.find_element(self.SEARCH_INPUT_USERNAME).send_keys(str)

    def count_users_in_table(self):
        rows = self.find_elements(self.USER_IN_TABLE)
        return len(rows)
    
    def click_search(self):
        self.find_element(self.SEARCH_BUTTON).click()

    def select_search_user_role(self, role):
        nth_child = 0
        self.find_element(self.USER_ROLE_DROPDOWN).click()

        if role == 'Admin':
            nth_child = 2
        if role == 'ESS':
            nth_child = 3
            
        dropdown = self.find_element((By.CSS_SELECTOR, f'div.oxd-select-dropdown.--positon-bottom > div:nth-child({nth_child}) > span'))
        dropdown.click()
     
    def get_first_employee_name(self):
        employee_name = self.find_element(self.FIRST_ELEMENT_USER_TABLE).text
        return employee_name
    
    def enter_employee_name(self, employee_name):
        input = self.find_element(self.SEARCH_INPUT_EMPLOYEE_NAME)
        input.send_keys(employee_name)
        self.find_element(self.EMPLOYEE_NAME_DROPDOWN).click()

    

