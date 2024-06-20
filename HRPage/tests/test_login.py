import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage

@pytest.fixture(scope="function")
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = "/usr/bin/google-chrome"
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()

def test_successful_login(driver):
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")
    assert "dashboard" in driver.current_url.lower()

def test_failed_login(driver):
    login_page = LoginPage(driver)
    login_page.login("wronguser", "wrongpasssword")
    assert "Invalid credentials" in login_page.get_error_message()

def test_required_error_message(driver):
    login_page = LoginPage(driver)
    login_page.login("", "")
    required_messages = login_page.get_required_error_message()
    assert "Required" in required_messages

def test_forgot_password_redirect(driver):
    login_page = LoginPage(driver)
    login_page.click_forgot_password()
    current_url = driver.current_url
    assert "requestPasswordResetCode" in current_url