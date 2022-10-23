from pages.base_page import BasePage
from pages.locators import OrderPageLocators as opl
import env
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains


# Класс для хранения тестовых данных для первой формы заказа
class FirstFormData:
    def __init__(self, name, last_name, address, metro_locator_tuple):
        self.name = name
        self.last_name = last_name
        self.address = address
        self.metro_locator_tuple = metro_locator_tuple


# Класс для хранения тестовых данных для второй формы заказа
class SecondFormData:
    def __init__(self, date, rent_period, color):
        self.date = date
        self.rent_period = rent_period
        self.color = color


CLIENT_DATA_SET_1 = FirstFormData(env.NAME_1, env.LAST_NAME_1, env.ADDRESS_1, opl.METRO_DINAMO)
CLIENT_DATA_SET_2 = FirstFormData(env.NAME_2, env.LAST_NAME_2, env.ADDRESS_2, opl.METRO_SHABOLOVSKAYA)

RENT_DATA_SET_1 = SecondFormData(env.TOMORROW, opl.TIME_2_DAYS, opl.COLOR_BLACK)
RENT_DATA_SET_2 = SecondFormData(env.IN_ONE_WEEK, opl.TIME_1_WEEK, opl.COLOR_GRAY)


class OrderPage(BasePage):
    def wait_for_load_order_page(self):
        submit_button = self.driver.find_element(*opl.SUBMIT_BUTTON_1)
        WebDriverWait(self.driver, 3).until(ec.element_to_be_clickable(submit_button))

    def submit_client_form(self, form_data: FirstFormData):
        self.driver.find_element(*opl.NAME_FIELD).send_keys(form_data.name)
        self.driver.find_element(*opl.LAST_NAME_FIELD).send_keys(form_data.last_name)
        self.driver.find_element(*opl.ADDRESS_FIELD).send_keys(form_data.address)
        self.driver.find_element(*opl.METRO_FIELD).click()
        self.driver.find_element(*form_data.metro_locator_tuple).click()
        self.driver.find_element(*opl.PHONE_NUMBER_FIELD).send_keys(env.PHONE_NUMBER)
        self.driver.find_element(*opl.SUBMIT_BUTTON_1).click()

    def submit_rent_details_form(self, form_data: SecondFormData):
        self.driver.find_element(*opl.DATE_FIELD).send_keys(form_data.date)
        # Клик в произвольном месте страницы, чтобы закрыть выпадающий календарь:
        ActionChains(self.driver).move_by_offset(30, 100).click().perform()
        self.driver.find_element(*opl.TIME_DROPDOWN).click()
        self.driver.find_element(*form_data.rent_period).click()
        self.driver.find_element(*form_data.color).click()
        self.driver.find_element(*opl.SUBMIT_BUTTON_2).click()

