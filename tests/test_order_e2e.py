import allure
import env
from pages.locators import OrderPageLocators as opl
from pages.locators import HomePageLocators as mpl
from pages import order_page as op


# Два тестовых класса для е2е тестов заказа самоката с разными наборами данных
@allure.feature('E2E_1')
@allure.description('Заказ на завтра, на срок в два дня, самокат черного цвета')
class TestOrderE2E1:

    @allure.title('Открытие страницы заказа')
    @allure.step("Нажать на кнопку 'Заказать' в хэдере")
    def test_press_order_button_top_open_order_form(self, home_page_class):
        home_page_class.driver.find_element(*mpl.ORDER_BUTTON_TOP).click()
        assert home_page_class.driver.current_url == env.ORDER_PAGE

    @allure.title('Заполнение данных о заказчике')
    @allure.step("Заполнить первую форму заказа")
    def test_fill_1st_order_form(self, order_page_class):
        order_page_class.submit_client_form(op.CLIENT_DATA_SET_1)
        assert order_page_class.driver.find_element(*opl.TITLE).text == 'Про аренду'

    @allure.title('Заполнение данных об аренде')
    @allure.step("Заполнить вторую форму заказа")
    def test_fill_2nd_order_form(self, order_page_class):
        order_page_class.submit_rent_details_form(op.RENT_DATA_SET_1)
        assert order_page_class.driver.find_element(*opl.ORDER_CONFIRMATION).text == 'Хотите оформить заказ?\n '

    @allure.title('Подтверждение заказа')
    @allure.step("Подтвердить заказ")
    def test_submit_order(self, order_page_class):
        order_page_class.driver.find_element(*opl.CONFIRM_BUTTON).click()
        assert 'Заказ оформлен' in order_page_class.driver.find_element(*opl.CONFIRMATION_MESSAGE).text


@allure.feature('E2E_2')
@allure.description('Заказ на следующую неделю, на срок в семь дней, самокат серого цвета')
class TestOrderE2E2:
    @allure.title('Открытие страницы заказа')
    @allure.step("Нажать на кнопку 'Заказать' внизу страницы")
    def test_press_order_button_top_open_order_form(self, home_page_class):
        home_page_class.driver.find_element(*mpl.ORDER_BUTTON_BOTTOM).click()
        assert home_page_class.driver.current_url == env.ORDER_PAGE

    @allure.title('Заполнение данных о заказчике')
    @allure.step("Заполнить первую форму заказа")
    def test_fill_1st_order_form(self, order_page_class):
        order_page_class.submit_client_form(op.CLIENT_DATA_SET_2)
        assert order_page_class.driver.find_element(*opl.TITLE).text == 'Про аренду'

    @allure.title('Заполнение данных об аренде')
    @allure.step("Заполнить вторую форму заказа")
    def test_fill_2nd_order_form(self, order_page_class):
        order_page_class.submit_rent_details_form(op.RENT_DATA_SET_2)
        assert order_page_class.driver.find_element(*opl.ORDER_CONFIRMATION).text == 'Хотите оформить заказ?\n '

    @allure.title('Подтверждение заказа')
    @allure.step("Подтвердить заказ")
    def test_submit_order(self, order_page_class):
        order_page_class.driver.find_element(*opl.CONFIRM_BUTTON).click()
        assert 'Заказ оформлен' in order_page_class.driver.find_element(*opl.CONFIRMATION_MESSAGE).text
