import pytest
import time
from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.admin_navigation import AdminNavigation
from pages.login_page import LoginPage
from pages.user_management_page import UserManagement

fake = Faker()

@pytest.fixture(scope="module")
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = '/usr/bin/google-chrome'
    chrome_options.add_argument("--lang=en-US")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()

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


@pytest.mark.parametrize("employee_name, username, password, user_role", 
                         [('a', fake.user_name(), fake.password(), 'Admin'),
                          ('a', fake.user_name(), "P@ssword456", 'ESS')])
def test_add_users(driver, employee_name, username, password, user_role):
    user_management = UserManagement(driver)
    user_management.go_to_add_user()
    user_management.add_new_user(employee_name, username, password, user_role)
    user_management.submit_user_form()
    assert user_management.validate_username_in_table(username)

def test_required_all_empty(driver):
    user_management = UserManagement(driver)
    user_management.go_to_add_user()
    user_management.submit_user_form()
    time.sleep(3)
    assert user_management.validate_required_all_fields()

def test_required_error_messqge_password(driver):
    user_management = UserManagement(driver)
    user_management.go_to_add_user()
    user_management.submit_user_form()
    assert "Required" == user_management.validate_password_error()

def test_should_be_5_characters_username(driver):
    user_management = UserManagement(driver)
    user_management.go_to_add_user()
    user_management.add_username('abc')
    assert "Should be at least 5 characters" == user_management.validate_should_be_at_least_5_characters_username()

def test_passwords_do_not_match(driver):
    user_management = UserManagement(driver)
    user_management.go_to_add_user()
    user_management.enter_password("Terrada5224")
    user_management.enter_confirm_password("terr")
    assert "Passwords do not match" == user_management.validate_passwords_do_not_match()

def test_password_at_least_7_char(driver):
    user_management = UserManagement(driver)
    user_management.go_to_add_user()
    user_management.enter_password('qwe')
    assert "Should have at least 7 characters" == user_management.validate_password_error()

def test_password_must_contain_1_number(driver):
    user_management = UserManagement(driver)
    user_management.go_to_add_user()
    user_management.enter_password('qwertywee')
    assert "Your password must contain minimum 1 number" == user_management.validate_password_error()

def test_password_strength_very_weak(driver):
    user_management = UserManagement(driver)
    user_management.go_to_add_user()
    user_management.clear_password_field()
    user_management.enter_password('acx')
    assert user_management.wait_password_strength_label_text('Very Weak')

def test_password_strength_weak(driver):
    user_management = UserManagement(driver)
    user_management.go_to_add_user()
    user_management.clear_password_field()
    user_management.enter_password('Terrada')
    assert user_management.wait_password_strength_label_text("Weak")

def test_password_strength_better(driver):
    user_management = UserManagement(driver)
    user_management.go_to_add_user()
    user_management.clear_password_field()
    user_management.enter_password('Terrada1')
    assert user_management.wait_password_strength_label_text('Better')

def test_password_strength_strong(driver):
    user_management = UserManagement(driver)
    user_management.go_to_add_user()
    user_management.clear_password_field()
    user_management.enter_password('Terrada123')
    assert user_management.wait_password_strength_label_text('Strong')

def test_password_strength_strongest(driver):
    user_management = UserManagement(driver)
    user_management.go_to_add_user()
    user_management.clear_password_field()
    user_management.enter_password('!Terrada5224')
    assert user_management.wait_password_strength_label_text('Strongest')

def test_username_already_exists(driver):
    user_management = UserManagement(driver)
    user_management.go_to_users()
    user_name = user_management.find_first_non_admin_username()
    user_management.click_add_user()
    user_management.add_username(user_name)
    assert user_management.validate_already_exists_error('Already exists')

def test_search_by_username(driver):
    user_management = UserManagement(driver)
    user_management.go_to_users()
    userName = user_management.find_first_non_admin_username()
    user_management.enter_username_search(userName)
    user_management.click_search()
    row_count = user_management.count_users_in_table()
    assert 1 == row_count

@pytest.mark.parametrize("user_role", ["Admin", "ESS"])
def test_search_by_user_role(driver, user_role):
    user_management = UserManagement(driver)
    user_management.go_to_users()
    user_management.select_search_user_role(user_role)
    user_management.click_search()
    assert user_management.validate_user_role(user_role)

def test_search_by_employee_name(driver):
    user_management = UserManagement(driver)
    user_management.go_to_users()
    employee_name = user_management.get_first_employee_name()
    user_management.enter_employee_name(employee_name)
    user_management.click_search()
    assert user_management.validate_employee_name(employee_name)

def test_delete_by_user_name(driver):
    user_management = UserManagement(driver)
    user_management.go_to_users()
    user_name = user_management.find_first_non_admin_username()
    user_management.enter_username_search(user_name)
    user_management.click_search()
    user_management.click_trash_can()
    user_management.click_yes_delete()
    assert False == user_management.validate_username_in_table(user_name)

def test_navigate_edit_user(driver):
    user_management = UserManagement(driver)
    driver.refresh()
    user_name = user_management.find_first_non_admin_username()
    user_management.enter_username_search(user_name)
    user_management.click_search()
    user_management.click_edit_pencil()
    assert user_management.edit_main_title()