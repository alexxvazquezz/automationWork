from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".oxd-alert-content--error")
    REQUIRED_ERROR_MESSAGE = (By.CSS_SELECTOR, ".oxd-input-field-error-message")
    FORGOT_PASSWORD_LINK = (By.CSS_SELECTOR, ".orangehrm-login-forgot-header")

    def __init__(self, driver):
        super().__init__(driver)
        self.go_to("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def login(self, username, password):
        self.find_element(self.USERNAME_INPUT).send_keys(username)
        self.find_element(self.PASSWORD_INPUT).send_keys(password)
        self.find_element(self.LOGIN_BUTTON).click()

    def get_error_message(self):
        return self.find_element(self.ERROR_MESSAGE).text
    
    def get_required_error_message(self):
        return [element.text for element in self.find_elements(self.REQUIRED_ERROR_MESSAGE)]
    
    def click_forgot_password(self):
        self.find_element(self.FORGOT_PASSWORD_LINK).click()
