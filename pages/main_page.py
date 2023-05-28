import pytest
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
    def wait_load_questions_important(self):
        WebDriverWait(self.driver,3).until(expected_conditions.visibility_of_element_located
                                           ((self.title_questions_important)))

    #Получение значения заголовка раздела "Вопросы о важном"
    def get_title_questions_important(self):
        return self.driver.find_element(*self.title_questions_important).text

    def wait_load_question_1(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located
                                            (self.question_1))

    def click_question_1(self):
        self.driver.find_element(*self.question_1).click()

    def wait_load_questions_answer_1(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located
                                            (self.answer_1))
    #def check_answer_to_question_1(self):
        #self.driver.find_element(*self.answer_1).text

    def check_answer_to_question(self, question, answer):
        WebDriverWait(self.driver,3).until(expected_conditions.visibility_of_element_located((question)))
        self.driver.find_element(*question).click()
        WebDriverWait(self.driver,3).until(expected_conditions.visibility_of_element_located((answer)))
        return self.driver.find_element(*answer).text


expected_class_1 = "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
expected_class_2 = "Пока что у нас так: один заказ — один самокат. " \
                       "Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."
expected_class_3 = "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. " \
                       "Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. " \
                       "Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
expected_class_4 = "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
expected_class_5 = "Пока что нет! " \
                       "Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
expected_class_6 = "Самокат приезжает к вам с полной зарядкой. " \
                       "Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. " \
                       "Зарядка не понадобится."
expected_class_7 = "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. " \
                       "Все же свои."
expected_class_8 = "Да, обязательно. Всем самокатов! И Москве, и Московской области."


class TestMainPage:

    def test_section_questions(self, driver):
        main_page = MainPageScooter(driver)
        driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page.scroll_end_main_page()
        main_page.wait_load_questions_important()
        title = main_page.get_title_questions_important()
        assert title == 'Вопросы о важном'

    @pytest.mark.parametrize(
        'question, answer',
        [
            [[By.ID, 'accordion__heading-0'],[By.ID, 'accordion__panel-0'],  ],
        ]
    )
    def test_answer_to_question_1(self, driver, question, answer):
        main_page = MainPageScooter(driver)
        driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page.scroll_end_main_page()
        main_page.check_answer_to_question(question, answer)