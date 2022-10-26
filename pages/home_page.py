from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from pages.locators import HomePageLocators as hpl
from pages.locators import FaqLocators as fl
import env


class HomePage:
    URL = 'https://qa-scooter.praktikum-services.ru/'

    FAQ_DATA = [
        (fl.QUESTION_1, fl.ANSWER_1, env.EXPECTED_ANSWER_1), (fl.QUESTION_2, fl.ANSWER_2, env.EXPECTED_ANSWER_2),
        (fl.QUESTION_3, fl.ANSWER_3, env.EXPECTED_ANSWER_3), (fl.QUESTION_4, fl.ANSWER_4, env.EXPECTED_ANSWER_4),
        (fl.QUESTION_5, fl.ANSWER_5, env.EXPECTED_ANSWER_5), (fl.QUESTION_6, fl.ANSWER_6, env.EXPECTED_ANSWER_6),
        (fl.QUESTION_7, fl.ANSWER_7, env.EXPECTED_ANSWER_7), (fl.QUESTION_8, fl.ANSWER_8, env.EXPECTED_ANSWER_8)
    ]

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.driver.implicitly_wait(timeout)

    def wait_for_load_home_page(self):
        cookie = self.driver.find_element(*hpl.ACCEPT_COOKIES)
        WebDriverWait(self.driver, 3).until(ec.element_to_be_clickable(cookie))

    def accept_cookies(self):
        self.driver.find_element(*hpl.ACCEPT_COOKIES).click()
