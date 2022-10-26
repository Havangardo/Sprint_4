import pytest
from selenium import webdriver
from pages.home_page import HomePage
from pages.order_page import OrderPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


# Фикстура, которая возвращает драйвер с открытой домашней страницей и принимает куки
@pytest.fixture
def home_page(driver):
    home_page = HomePage(driver)
    driver.get(home_page.URL)
    home_page.wait_for_load_home_page()
    home_page.accept_cookies()
    return home_page


# Фикстура, которая возвращает драйвер с открытой страницей заказа
@pytest.fixture
def order_page(home_page):
    order_page = OrderPage(home_page.driver)
    order_page.driver.get(order_page.URL)
    order_page.wait_for_load_order_page()
    return order_page
