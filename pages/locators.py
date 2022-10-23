from selenium.webdriver.common.by import By


class HeaderLocators:
    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    # Кнопка "Войти" на главной Дзена для проверки загрузки страницы после редиректа
    YA_LOGIN = (By.XPATH, ".//span[@class='zen-ui-button-text__text']")


class HomePageLocators:
    ORDER_BUTTON_TOP = (By.XPATH, ".//button[@class='Button_Button__ra12g']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    ACCEPT_COOKIES = (By.ID, "rcc-confirm-button")


class FaqLocators:
    QUESTION_1 = (By.ID, "accordion__heading-0")
    ANSWER_1 = (By.ID, "accordion__panel-0")
    QUESTION_2 = (By.ID, "accordion__heading-1")
    ANSWER_2 = (By.ID, "accordion__panel-1")
    QUESTION_3 = (By.ID, "accordion__heading-2")
    ANSWER_3 = (By.ID, "accordion__panel-2")
    QUESTION_4 = (By.ID, "accordion__heading-3")
    ANSWER_4 = (By.ID, "accordion__panel-3")
    QUESTION_5 = (By.ID, "accordion__heading-4")
    ANSWER_5 = (By.ID, "accordion__panel-4")
    QUESTION_6 = (By.ID, "accordion__heading-5")
    ANSWER_6 = (By.ID, "accordion__panel-5")
    QUESTION_7 = (By.ID, "accordion__heading-6")
    ANSWER_7 = (By.ID, "accordion__panel-6")
    QUESTION_8 = (By.ID, "accordion__heading-7")
    ANSWER_8 = (By.ID, "accordion__panel-7")


class OrderPageLocators:
    # Форма на 1й странице
    NAME_FIELD = (By.XPATH, ".//input[(@class='Input_Input__1iN_Z Input_Responsible__1jDKN' and @placeholder='* Имя')]")
    LAST_NAME_FIELD = (By.XPATH, ".//input[(@class='Input_Input__1iN_Z Input_Responsible__1jDKN' "
                                 "and @placeholder='* Фамилия')]")
    ADDRESS_FIELD = (By.XPATH, ".//input[(@class='Input_Input__1iN_Z Input_Responsible__1jDKN' "
                               "and @placeholder='* Адрес: куда привезти заказ')]")
    METRO_FIELD = (By.CLASS_NAME, "select-search__input")
    METRO_DINAMO = (By.XPATH, ".//li[@data-index='27']")
    METRO_SHABOLOVSKAYA = (By.XPATH, ".//li[@data-index='92']")
    PHONE_NUMBER_FIELD = (By.XPATH, ".//input[(@class='Input_Input__1iN_Z Input_Responsible__1jDKN' "
                                    "and @placeholder='* Телефон: на него позвонит курьер')]")
    SUBMIT_BUTTON_1 = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")

    # Форма на 2й странице
    # Заголовок для проверки, что первая форма заполнена успешно:
    TITLE = (By.CLASS_NAME, "Order_Header__BZXOb")
    DATE_FIELD = (By.XPATH, ".//input[(@class='Input_Input__1iN_Z Input_Responsible__1jDKN' "
                            "and @placeholder='* Когда привезти самокат')]")
    TIME_DROPDOWN = (By.CLASS_NAME, "Dropdown-control")
    TIME_2_DAYS = (By.XPATH, ".//div[(@class='Dropdown-option' and text()='двое суток')]")
    TIME_1_WEEK = (By.XPATH, ".//div[(@class='Dropdown-option' and text()='семеро суток')]")
    COLOR_BLACK = (By.ID, "black")
    COLOR_GRAY = (By.ID, "grey")
    SUBMIT_BUTTON_2 = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")

    # Выпадающее окно "Хотите оформить заказ?"
    ORDER_CONFIRMATION = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")
    CONFIRM_BUTTON = (By.XPATH, ".//button[(@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Да')]")

    # Заказ оформлен
    CONFIRMATION_MESSAGE = (By.XPATH, ".//div[@class='Order_ModalHeader__3FDaJ']")
