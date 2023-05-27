from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time

class MainPageScooter:
    title_questions_important = [By.XPATH,
                                 './/div[@class = "Home_FourPart__1uthg"]/div[@class = "Home_SubHeader__zwi_E"]']
    question_1 = [By.ID, 'accordion__heading-0']
    answer_1 = [By.ID, 'accordion__panel-0']

    question_important_2 = [By.ID, 'accordion__heading-1']
    answer_2 = [By.ID, 'accordion__panel-1']

    question_3 = [By.ID, 'accordion__heading-2']
    answer_3 = [By.ID, 'accordion__panel-2']

    question_4 = [By.ID, 'accordion__heading-3']
    answer_4 = [By.ID, 'accordion__panel-3']

    questions_5 = [By.ID, 'accordion__heading-4']
    answer_5 = [By.ID, 'accordion__panel-4']

    questions_6 = [By.ID, 'accordion__heading-5']
    answer_6 = [By.ID, 'accordion__panel-5']

    questions_7 = [By.ID, 'accordion__heading-6']
    answer_7 = [By.ID, 'accordion__panel-6']

    questions_8 = [By.ID, 'accordion__heading-7']
    answer_8 = [By.ID, 'accordion__panel-7']
    def __init__(self, driver):
        self.driver = driver

    #Скролл до конца страницы
    def scroll_end_main_page(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #Ожидание загрузки раздела "Вопросы о важном"
    def wait_for_load_questions_important(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located
                                            (self.title_questions_important))
    #Получение значения заголовка раздела "Вопросы о важном"
    def get_title_questions_important(self):
        return self.driver.find_element(*self.title_questions_important).text

    def check_title_questions_important(self):
        self.scroll_end_main_page()
        self.wait_for_load_questions_important()

    def check_answer_to_question_1(self):
        self.driver.find_element(*self.question_1).click()
        return self.driver.find_element(*self.answer_1).text

expected_class_1 = "Сутки — 400 рублей. Оплата курьеру — наличными или картой."

class TestMainPage:

    driver = None
    @classmethod
    def setup_class(cls):
        # создали драйвер для браузера Chrome
        cls.driver = webdriver.Firefox()

    def test_get_title_questions_important(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page = MainPageScooter(self.driver)
        main_page.scroll_end_main_page()
        main_page.wait_for_load_questions_important()
        assert main_page.get_title_questions_important() == 'Вопросы о важном'

    def test_check_iq_1(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page = MainPageScooter(self.driver)
        main_page.check_title_questions_important()
        print(main_page.check_answer_to_question_1())

    @classmethod
    def teardown_class(cls):
        # закрой браузер
        cls.driver.quit()