import allure
import pytest
from pages.home_page import HomePage as hp


@allure.feature('FAQ')
@allure.description('Проверка верных ответов на вопросы в FAQ')
class TestFaq:
    @pytest.mark.parametrize('question,answer,expected_answer', hp.FAQ_DATA)
    def test_faq(self, home_page, question, answer, expected_answer):
        home_page.driver.find_element(*question).click()
        assert home_page.driver.find_element(*answer).text == expected_answer
