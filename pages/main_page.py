from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure

class MainPageScooter(BasePage):

    def __init__(self, driver):
        self.driver = driver

    logo_yandex = [By.XPATH, './/img[@alt = "Yandex"]//ancestor::a']
    page_yandex = [By.XPATH, './/button[text() ="Найти"]']

    @allure.step('Получаем ответ на вопрос в блоке "Вопросы о важном"')
    def get_answer_to_question(self, question, answer):
        self.wait_load_any_element(locator=question)
        self.driver.find_element(*question).click()
        self.wait_load_any_element(locator=answer)
        return self.driver.find_element(*answer).text

    @allure.step('Кликаем по логотипу "Яндекса"')
    def click_logo_yandex(self):
        self.wait_load_any_element(locator=self.logo_yandex)
        self.driver.find_element(*self.logo_yandex).click()
        self.switch_to_windows()
        self.wait_load_any_element(locator=self.page_yandex)
