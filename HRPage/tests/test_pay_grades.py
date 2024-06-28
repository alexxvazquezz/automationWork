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
    pay_grades = PayGrades(driver)
    admin_page.go_to_pay_grades()
    assert "Pay Grades" == pay_grades.main_header_text()