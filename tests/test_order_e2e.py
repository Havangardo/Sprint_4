import allure
from pages.locators import OrderPageLocators as opl
from pages.locators import HomePageLocators as hpl
from pages.order_page import OrderPage as op


class TestOrderE2E:
    @allure.title('Позитивный Е2Е-тест заказа самоката')
    @allure.description('Заказ на завтра, на срок в два дня, самокат черного цвета')
    def test_e2e_order_set1(self, home_page, order_page):
        home_page.driver.find_element(*hpl.ORDER_BUTTON_TOP).click()
        order_page.driver.refresh()
        order_page.submit_client_form(op.CLIENT_FORM_DATA_1)
        order_page.submit_rent_details_form(op.RENT_FORM_DATA_1)
        order_page.driver.find_element(*opl.CONFIRM_BUTTON).click()
        assert 'Заказ оформлен' in order_page.driver.find_element(*opl.CONFIRMATION_MESSAGE).text

    @allure.title('Позитивный Е2Е-тест заказа самоката')
    @allure.description('Заказ на следующую неделю, на срок в семь дней, самокат серого цвета')
    def test_e2e_order_set2(self, home_page, order_page):
        home_page.driver.find_element(*hpl.ORDER_BUTTON_BOTTOM).click()
        order_page.driver.refresh()
        order_page.submit_client_form(op.CLIENT_FORM_DATA_2)
        order_page.submit_rent_details_form(op.RENT_FORM_DATA_2)
        order_page.driver.find_element(*opl.CONFIRM_BUTTON).click()
        assert 'Заказ оформлен' in order_page.driver.find_element(*opl.CONFIRMATION_MESSAGE).text
