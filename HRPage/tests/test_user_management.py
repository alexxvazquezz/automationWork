import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.admin_navigation import AdminNavigation
from pages.login_page import LoginPage
from pages.user_management_page import UserManagement

@pytest.fixture(scope="module")
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = '/usr/bin/google-chrome'
    chrome_options.add_argument("--lang=en-US")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Perform login once
    loging_page = LoginPage(driver)
    loging_page.login("Admin", "admin123")

    yield driver
    driver.quit()

def test_navigate_to_user_management(driver):
    admin_page = AdminNavigation(driver)
    user_management = UserManagement(driver)
    admin_page.click_admin_side_bar()
    admin_page.go_to_users()

    main_title_user_management = user_management.main_title_text()
    assert "System Users" == main_title_user_management

def test_add_user_admin(driver):
    user_management = UserManagement(driver)
    user_management.click_add_user()
    user_management.clik_user_role_dropdown()
    user_management.add_admin_input_value()
    user_management.enter_employee_name('a')
    time.sleep(2)
    user_management.click_value_employee_name()
    user_management.click_status_dropdown()
    user_management.click_status_enabled()
    user_management.add_username('Louki45')
    user_management.enter_password('!Terrada5224')
    user_management.enter_confirm_password('!Terrada5224')
    user_management.click_save()
    time.sleep(5)


