import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.time_page import TimePage
from pages.leave_page import LeavePage

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

def test_is_on_dashboard(driver):
    dashboard_page = DashboardPage(driver)
    assert dashboard_page.is_on_dashboard(), "Not on the dashboar page"
    
def test_navigate_to_time(driver):
    dashboard_page = DashboardPage(driver)
    time_page = TimePage(driver)
    dashboard_page.click_time_clock()

    main_title_time_page = time_page.main_title_text()
    assert "Punch In" == main_title_time_page
    driver.back()

def test_navigate_to_leave_assign(driver):
    dashboard_page = DashboardPage(driver)
    leave_page = LeavePage(driver)
    dashboard_page.click_assign_leave()
    
    main_title_leave_page = leave_page.main_title_text()
    assert "Assign Leave" == main_title_leave_page
    driver.back()

def test_navigate_to_leave(driver):
    dashboard_page = DashboardPage(driver)
    leave_page = LeavePage(driver)
    dashboard_page.click_leave_list()

    main_title_leave_page = leave_page.leave_list_title()
    assert "Leave List" == main_title_leave_page
    driver.back()

def test_navigate_to_timesheet(driver):
    dashboard_page = DashboardPage(driver)
    time_page = TimePage(driver)
    dashboard_page.click_timesheet()
    
    main_title_timesheet = time_page.main_title_text()
    assert "Select Employee" == main_title_timesheet
    driver.back()

def test_navigate_apply_leave(driver):
    dashboard_page = DashboardPage(driver)
    leave_page = LeavePage(driver)
    dashboard_page.click_apply_leave()

    main_title_apply = leave_page.main_title_text()
    assert "Apply Leave" == main_title_apply
    driver.back()

def test_navigate_my_leave(driver):
    dashboard_page = DashboardPage(driver)
    leave_page = LeavePage(driver)
    dashboard_page.click_my_leave()

    main_title = leave_page.leave_list_title()
    assert "My Leave List" == main_title
    driver.back()

def test_navigate_my_timesheet(driver):
    dashboard_page = DashboardPage(driver)
    time_page = TimePage(driver)
    dashboard_page.click_my_timesheet()

    main_title = time_page.main_title_text()
    assert "My Timesheet" == main_title
    driver.back()