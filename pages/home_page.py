from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from pages.locators import HomePageLocators as hpl


class HomePage(BasePage):
    def wait_for_load_home_page(self):
        cookie = self.driver.find_element(*hpl.ACCEPT_COOKIES)
        WebDriverWait(self.driver, 3).until(ec.element_to_be_clickable(cookie))

    def accept_cookies(self):
        self.driver.find_element(*hpl.ACCEPT_COOKIES).click()
