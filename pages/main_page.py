import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class MainPageScooter:

    title_questions_important = [By.XPATH,
                                 './/div[@class = "Home_FourPart__1uthg"]/div[@class = "Home_SubHeader__zwi_E"]']
    def __init__(self, driver):
        self.driver = driver

    #Скролл до конца страницы
    def scroll_end_main_page(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    #Ожидание загрузки раздела "Вопросы о важном"
    def wait_load_questions_important(self):
        WebDriverWait(self.driver,3).until(expected_conditions.visibility_of_element_located
                                           ((self.title_questions_important)))
    def get_title_questions_important(self):
        return self.driver.find_element(*self.title_questions_important).text
    def check_answer_to_question(self, question, answer):
        WebDriverWait(self.driver,3).until(expected_conditions.visibility_of_element_located((question)))
        self.driver.find_element(*question).click()
        WebDriverWait(self.driver,3).until(expected_conditions.visibility_of_element_located((answer)))
        return self.driver.find_element(*answer).text
