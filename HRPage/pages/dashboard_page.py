from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from config import BASE_URL

class DashboardPage(BasePage):
    CLOCK_BUTTON = (By.CSS_SELECTOR, ".orangehrm-attendance-card-action")
    ASSIGN_LEAVE_ICON = (By.CSS_SELECTOR, "div:nth-child(3) > div > div.orangehrm-dashboard-widget-body > div > div:nth-child(1) > button")
    LEAVE_LIST_ICON = (By.CSS_SELECTOR, "div:nth-child(3) > div > div.orangehrm-dashboard-widget-body > div > div:nth-child(2) > button")
    TIMESHEET_ICON = (By.CSS_SELECTOR, "div:nth-child(3) > div > div.orangehrm-dashboard-widget-body > div > div:nth-child(3) > button")
    APPLY_LEAVE_ICON = (By.CSS_SELECTOR, "div:nth-child(3) > div > div.orangehrm-dashboard-widget-body > div > div:nth-child(4) > button")
    MY_LEAVE_ICON = (By.CSS_SELECTOR, "div:nth-child(3) > div > div.orangehrm-dashboard-widget-body > div > div:nth-child(5) > button")
    MY_TIMESHEET = (By.CSS_SELECTOR, "div:nth-child(3) > div > div.orangehrm-dashboard-widget-body > div > div:nth-child(6) > button")

    def __init__(self, driver):
        super().__init__(driver)

    def is_on_dashboard(self):
        return self.find_element(self.CLOCK_BUTTON)
    
    def go_to_dashboard(self):
        self.go_to(f"{BASE_URL}/dashboard/index")
    
    def click_time_clock(self):
        self.find_element(self.CLOCK_BUTTON).click()

    def click_assign_leave(self):
        self.find_element(self.ASSIGN_LEAVE_ICON).click()
    
    def click_leave_list(self):
        self.find_element(self.LEAVE_LIST_ICON).click()
    
    def click_timesheet(self):
        self.find_element(self.TIMESHEET_ICON).click()
    
    def click_apply_leave(self):
        self.find_element(self.APPLY_LEAVE_ICON).click()

    def click_my_leave(self):
        self.find_element(self.MY_LEAVE_ICON).click()

    def click_my_timesheet(self):
        self.find_element(self.MY_TIMESHEET).click()

    