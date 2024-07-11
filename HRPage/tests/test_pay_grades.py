import pytest
import time
import os
from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.admin_navigation import AdminNavigation
from pages.login_page import LoginPage
from pages.pay_grades_page import PayGrades

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

def test_navigate_to_pay_grade(driver):
    admin_page = AdminNavigation(driver)
    pay_grades = PayGrades(driver)
    admin_page.go_to_pay_grades()
    assert "Pay Grades" == pay_grades.main_header_text()

def test_navigate_to_add_pay_grade(driver):
    pay_grades = PayGrades(driver)
    pay_grades.go_to_pay_grades()
    pay_grades.click_add_button()
    assert "Add Pay Grade" == pay_grades.add_pay_grade_main_header_text()

def test_add_pay_grade_required_field(driver):
    pay_grades = PayGrades(driver)
    pay_grades.go_to_add_pay_grade()
    pay_grades.click_save_pay_grade_button()
    assert "Required" == pay_grades.required_error_text_add_pay_grade()

def test_add_pay_grade_redirect(driver):
    pay_grades = PayGrades(driver)
    pay_grades.go_to_add_pay_grade()
    name = fake.name()
    pay_grades.add_pay_grade(name)
    assert pay_grades.edit_pay_grade_header()
