import pytest
import time
import os
from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.admin_navigation import AdminNavigation
from pages.login_page import LoginPage
from pages.job_title_page import JobTitle

fake = Faker()
file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Test_doc.pdf'))

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
    job_title = JobTitle(driver)
    admin_page.click_admin_side_bar()
    admin_page.go_to_job_titles()
    assert "Job Titles" == job_title.main_title()

def test_navigate_add_job_title(driver):
    job_title = JobTitle(driver)
    job_title.click_add_button()
    assert "Add Job Title" == job_title.main_title_add_job_title()

def test_required_field_add_job_title(driver):
    admin_page = AdminNavigation(driver)
    job_title = JobTitle(driver)
    admin_page.click_admin_side_bar()
    admin_page.go_to_job_titles()
    job_title.click_add_button()
    job_title.click_save()
    assert 'Required' == job_title.required_error_message()

@pytest.mark.parametrize("job_title, description, file_path, note",
                         [(fake.name(), fake.paragraphs(), file_path, fake.paragraphs())])
def test_add_job_title(driver, job_title, description, file_path, note):
    job_titles = JobTitle(driver)
    job_titles.add_job_title(job_title, description, file_path, note)

    found = job_titles.validate_job_title(job_title)
    assert job_title == found

def test_delete(driver):
    job_titles = JobTitle(driver)
    # Get job title name that will be deleted to validate later
    job_title_name = job_titles.get_first_job_title_name_table_row()
    job_titles.click_first_trash_icon()
    job_titles.click_yes_delete()
    validate = job_titles.validate_job_title(job_title_name)
    assert False == validate
    
