import allure
import env
from pages.locators import HeaderLocators as hl
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class TestLogo:

    @allure.title('Проверка перехода по клику на логотип Самоката')
    @allure.description('При клике по лого Самоката на любой странице, кроме главной, произойдет редирект на главную.')
    def test_redirect_samocat_logo(self, home_page_func):
        home_page_func.driver.get(env.ORDER_PAGE)
        home_page_func.driver.find_element(*hl.SCOOTER_LOGO).click()
        assert home_page_func.driver.current_url == env.MAIN_PAGE

    @allure.title('Проверка перехода по клику на логотип Яндекса')
    @allure.description('При клике на лого Яндекс в новой вкладке откроется Яндекс.Дзен.')
    def test_redirect_yandex_logo(self, home_page_func):
        home_page_func.driver.find_element(*hl.YANDEX_LOGO).click()
        home_page_func.driver.switch_to.window(home_page_func.driver.window_handles[1])
        ya_login = home_page_func.driver.find_element(*hl.YA_LOGIN)
        WebDriverWait(home_page_func.driver, 3).until(ec.element_to_be_clickable(ya_login))
        assert home_page_func.driver.current_url == env.YANDEX_PAGE
