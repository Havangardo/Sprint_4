# Sprint_4
## Автотесты для сервиса Яндекс.Самокат

### [Яндекс.Самокат](https://qa-scooter.praktikum-services.ru/) - сервис для заказа электросамоката на дом.

Позитивные тесты (функциональные и е2е) с использованием Pytest, Selenium, Allure. Все тесты выполняются в Firefox.

Установить зависимости:

    pip install -r requirements.txt

Запуск отчета Allure. Выполнить в терминале PyCharm:

    pytest tests --alluredir=allure_results
    allure serve allure_results


