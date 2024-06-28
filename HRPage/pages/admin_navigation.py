from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AdminNavigation(BasePage):
    ADMIN_MENU_TITLE = (By.CSS_SELECTOR, '.oxd-topbar-header-breadcrumb > h6')
    SIDE_NAVE_ADMIN = (By.CSS_SELECTOR, 'div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(1) > a > span')
    USER_MANAGEMENT_DROPDOWN = (By.CSS_SELECTOR, 'li.oxd-topbar-body-nav-tab.--parent.--visited > span')
    USER_USER_MANAGEMENT = (By.CSS_SELECTOR, '.oxd-topbar-body-nav-tab-link')
    JOB_DROPDOWN = (By.CSS_SELECTOR, 'div.oxd-topbar-body > nav > ul > li:nth-child(2)')
    JOB_JOB_TITLES = (By.CSS_SELECTOR, 'a[href="#"][role="menuitem"].oxd-topbar-body-nav-tab-link')
    PAY_GRADES = (By.LINK_TEXT, 'Pay Grades')

    def __init__(self, driver):
        super().__init__(driver)

    def click_admin_side_bar(self):
        self.find_element(self.SIDE_NAVE_ADMIN).click()

    def click_job_dropdown(self):
        self.find_element(self.JOB_DROPDOWN).click()

    def click_job_titles(self):
        self.find_element(self.JOB_JOB_TITLES).click()

    def click_pay_grades(self):
        self.find_element(self.PAY_GRADES).click()

    def click_user_management_dropdown(self):
        self.find_element(self.USER_MANAGEMENT_DROPDOWN).click()

    def click_user_management(self):
        self.find_element(self.USER_USER_MANAGEMENT).click()


    def get_admin_menu_title(self):
        return self.find_element(self.ADMIN_MENU_TITLE).text
    
    def go_to_users(self):
        self.click_user_management_dropdown()
        self.click_user_management()

    def go_to_job_titles(self):
        self.click_job_dropdown()
        self.click_job_titles()

    def go_to_pay_grades(self):
        self.click_admin_side_bar()
        self.click_job_dropdown()
        self.click_pay_grades()

