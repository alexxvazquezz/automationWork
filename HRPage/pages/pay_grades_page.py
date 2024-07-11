from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from config import BASE_URL

class PayGrades(BasePage):
    MAIN_HEADER = (By.CSS_SELECTOR, 'div.orangehrm-header-container > h6')
    ADD_PAY_GRADE_HEADER = (By.CSS_SELECTOR, 'div.oxd-layout-context > div > div > h6')
    ADD_BUTTON = (By.CSS_SELECTOR, 'div.orangehrm-header-container > div > button > i')
    SAVE_PAY_GRADE_BUTTON = (By.CSS_SELECTOR, 'button.oxd-button.oxd-button--medium.oxd-button--secondary.orangehrm-left-space')
    ERROR_REQUIRED_PAY_GRADE = (By.CSS_SELECTOR, 'form > div.oxd-form-row > div > div > div > span')
    NAME_INPUT_PAY_GRADE = (By.CSS_SELECTOR, ' div:nth-child(2) > input')
    EDIT_PAY_GRADE_HEADER = (By.CSS_SELECTOR, 'div.oxd-layout-context > div:nth-child(1) > div > h6')

    def __init__(self, driver):
        super().__init__(driver)

    def main_header_text(self):
        text = self.find_element(self.MAIN_HEADER).text
        return text
    
    def add_pay_grade_main_header_text(self):
        text = self.find_element(self.ADD_PAY_GRADE_HEADER).text
        return text
    
    def go_to_pay_grades(self):
        self.go_to(f"{BASE_URL}/admin/viewPayGrades")

    def go_to_add_pay_grade(self):
        self.go_to(f"{BASE_URL}/admin/payGrade")
    
    def click_add_button(self):
        button = self.find_element(self.ADD_BUTTON)
        button.click()

    def click_save_pay_grade_button(self):
        button = self.find_element(self.SAVE_PAY_GRADE_BUTTON)
        button.click()

    def required_error_text_add_pay_grade(self):
        text = self.find_element(self.ERROR_REQUIRED_PAY_GRADE).text
        return text
    
    def input_pay_grade_name(self, str):
        input = self.find_element(self.NAME_INPUT_PAY_GRADE)
        input.send_keys(str)

    def add_pay_grade(self, str):
        self.input_pay_grade_name(str)
        self.click_save_pay_grade_button()

    def edit_pay_grade_header(self):
        return self.wait_for_text_change(self.EDIT_PAY_GRADE_HEADER, 'Edit Pay Grade')
        
    