from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AdminNavigation(BasePage):
    ADMIN_MENU_TITLE = (By.CSS_SELECTOR, '.oxd-topbar-header-breadcrumb > h6')
    SIDE_NAVE_ADMIN = (By.CSS_SELECTOR, 'div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(1) > a > span')
    USER_MANAGEMENT_DROPDOWN = (By.CSS_SELECTOR, 'li.oxd-topbar-body-nav-tab.--parent.--visited > span')
    USER_USER_MANAGEMENT = (By.CSS_SELECTOR, '.oxd-topbar-body-nav-tab-link')

    def __init__(self, driver):
        super().__init__(driver)

    def click_admin_side_bar(self):
        self.find_element(self.SIDE_NAVE_ADMIN).click()


    def get_admin_menu_title(self):
        return self.find_element(self.ADMIN_MENU_TITLE).text
    
    def go_to_users(self):
        self.find_element(self.USER_MANAGEMENT_DROPDOWN).click()
        self.find_element(self.USER_USER_MANAGEMENT).click()