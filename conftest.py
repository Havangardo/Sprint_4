import pytest
from selenium import webdriver
from pages.home_page import HomePage
from pages.order_page import OrderPage
import env


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


# Фикстура, которая возвращает драйвер с открытой домашней страницей (для обычных тестов)
@pytest.fixture
def home_page_func(driver):
    return main_page(driver)


# Драйвер для е2е тестов
@pytest.fixture(scope='class')
def driver_class():
    driver = webdriver.Firefox()
    driver.set_window_size(1100, 800)
    yield driver
    driver.quit()


# Фикстура, которая возвращает драйвер с открытой домашней страницей (для е2е тестов)
@pytest.fixture(scope="class")
def home_page_class():
    driver = webdriver.Firefox()
    driver.set_window_size(1100, 800)
    yield main_page(driver)
    driver.quit()


# Фикстура, которая возвращает драйвер с открытой страницей заказа (для е2е тестов)
@pytest.fixture(scope='class')
def order_page_class(home_page_class):
    order_page = OrderPage(home_page_class.driver, env.ORDER_PAGE)
    order_page.open()
    order_page.wait_for_load_order_page()
    return order_page


def main_page(driver):
    home_page = HomePage(driver, env.MAIN_PAGE)
    home_page.open()
    home_page.wait_for_load_home_page()
    home_page.accept_cookies()
    return home_page
