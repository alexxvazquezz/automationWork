from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class JobTitle(BasePage):
    MAIN_TITLE = (By.CSS_SELECTOR, 'div.orangehrm-header-container > h6')
    ADD_BUTTON = (By.CSS_SELECTOR, 'div.orangehrm-header-container > div > button')
    ADD_JOB_TITLE_MAIN_TITLE = (By.CSS_SELECTOR, 'h6.oxd-text.oxd-text--h6.orangehrm-main-title')
    SAVE_BUTTON = (By.CSS_SELECTOR, '.oxd-button--secondary.orangehrm-left-space')
    REQUIRED_ERROR_MESSAGE = (By.CSS_SELECTOR, 'span.oxd-text.oxd-text--span.oxd-input-field-error-message.oxd-input-group__message')
    INPUT_JOB_TITLE = (By.CSS_SELECTOR, 'div:nth-child(1) > div > div:nth-child(2) > input')
    JOB_DESCRIPTION = (By.CSS_SELECTOR, 'div:nth-child(2) > div > div:nth-child(2) > textarea')
    INPUT_FILE = (By.CSS_SELECTOR, 'input.oxd-file-input')
    ADD_NOTE = (By.CSS_SELECTOR, 'div:nth-child(4) > div > div:nth-child(2) > textarea')
    FIRST_ROW_JOB_TABLE_NAME = (By.CSS_SELECTOR, 'div.oxd-table-body > div:nth-child(1) > div > div:nth-child(2) > div')
    FIRST_ROW_TRASH_BUTTON = (By.CSS_SELECTOR, 'div:nth-child(1) > div > div:nth-child(4) > div > button:nth-child(1)')
    YES_DELETE_BUTTON = (By.CSS_SELECTOR, 'button.oxd-button.oxd-button--medium.oxd-button--label-danger.orangehrm-button-margin')

    def __init__(self, driver):
        super().__init__(driver)

    def main_title(self):
        text = self.find_element(self.MAIN_TITLE).text
        return text
    
    def click_add_button(self):
        button = self.find_element(self.ADD_BUTTON)
        button.click()

    def main_title_add_job_title(self):
        text = self.find_element(self.ADD_JOB_TITLE_MAIN_TITLE).text
        return text
    
    def click_save(self):
        button = self.find_element(self.SAVE_BUTTON)
        button.click()

    def required_error_message(self):
        text = self.find_element(self.REQUIRED_ERROR_MESSAGE).text
        return text
    
    def input_job_title(self, str):
        input = self.find_element(self.INPUT_JOB_TITLE)
        input.send_keys(str)
    
    def input_description(self, str):
        input = self.find_element(self.JOB_DESCRIPTION)
        input.send_keys(str)

    def input_file(self, file_path):
        file_input = self.find_element(self.INPUT_FILE)
        file_input.send_keys(file_path)

    def input_note(self, str):
        input = self.find_element(self.ADD_NOTE)
        input.send_keys(str)

    def validate_job_title(self, job_title):
        i = 1
        while True:
            nth_child_selector = f"div.oxd-table-body > div:nth-child({i}) > div > div:nth-child(2) > div"
            try:
                title_element = self.find_element((By.CSS_SELECTOR, nth_child_selector))
                if title_element.text == job_title:
                    found = title_element.text
                    return found
            except NoSuchElementException:
                break

            i += 1

        return False
    
    def add_job_title(self, job_title, description, file_path, note):
        self.input_job_title(job_title)
        self.input_description(description)
        self.input_file(file_path)
        self.input_note(note)
        self.click_save()

    def get_first_job_title_name_table_row(self):
        text = self.find_element(self.FIRST_ROW_JOB_TABLE_NAME).text
        return text
    
    def click_first_trash_icon(self):
        button = self.find_element(self.FIRST_ROW_TRASH_BUTTON)
        button.click()

    def click_yes_delete(self):
        button = self.find_element(self.YES_DELETE_BUTTON)
        button.click()