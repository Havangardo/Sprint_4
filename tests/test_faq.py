import allure
import env
from pages.locators import FaqLocators as fl


@allure.feature('FAQ')
@allure.description('Проверка верных ответов на вопросы в FAQ')
class TestFaq:
    @allure.title('Проверка выпадающего ответа на первый вопрос')
    def test_check_question_1(self, home_page_func):
        home_page_func.driver.find_element(*fl.QUESTION_1).click()
        assert home_page_func.driver.find_element(*fl.ANSWER_1).text == env.CORRECT_ANSWER_1

    @allure.title('Проверка выпадающего ответа на второй вопрос')
    def test_check_question_2(self, home_page_func):
        home_page_func.driver.find_element(*fl.QUESTION_2).click()
        assert home_page_func.driver.find_element(*fl.ANSWER_2).text == env.CORRECT_ANSWER_2

    @allure.title('Проверка выпадающего ответа на третий вопрос')
    def test_check_question_3(self, home_page_func):
        home_page_func.driver.find_element(*fl.QUESTION_3).click()
        assert home_page_func.driver.find_element(*fl.ANSWER_3).text == env.CORRECT_ANSWER_3

    @allure.title('Проверка выпадающего ответа на четвёртый вопрос')
    def test_check_question_4(self, home_page_func):
        home_page_func.driver.find_element(*fl.QUESTION_4).click()
        assert home_page_func.driver.find_element(*fl.ANSWER_4).text == env.CORRECT_ANSWER_4

    @allure.title('Проверка выпадающего ответа на пятый вопрос')
    def test_check_question_5(self, home_page_func):
        home_page_func.driver.find_element(*fl.QUESTION_5).click()
        assert home_page_func.driver.find_element(*fl.ANSWER_5).text == env.CORRECT_ANSWER_5

    @allure.title('Проверка выпадающего ответа на шестой вопрос')
    def test_check_question_6(self, home_page_func):
        home_page_func.driver.find_element(*fl.QUESTION_6).click()
        assert home_page_func.driver.find_element(*fl.ANSWER_6).text == env.CORRECT_ANSWER_6

    @allure.title('Проверка выпадающего ответа на седьмой вопрос')
    def test_check_question_7(self, home_page_func):
        home_page_func.driver.find_element(*fl.QUESTION_7).click()
        assert home_page_func.driver.find_element(*fl.ANSWER_7).text == env.CORRECT_ANSWER_7

    @allure.title('Проверка выпадающего ответа на восьмой вопрос')
    def test_check_question_8(self, home_page_func):
        home_page_func.driver.find_element(*fl.QUESTION_8).click()
        assert home_page_func.driver.find_element(*fl.ANSWER_8).text == env.CORRECT_ANSWER_8
