from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage


class MainPageScooter(BasePage):

    def __init__(self, driver):
        self.driver = driver

    logo_yandex = [By.XPATH, './/img[@alt = "Yandex"]//ancestor::a']
    page_yandex = [By.XPATH, './/button[text() ="Найти"]']

    def get_answer_to_question(self, question, answer):
        self.wait_load_any_element(locator=question)
        self.driver.find_element(*question).click()
        self.wait_load_any_element(locator=answer)
        return self.driver.find_element(*answer).text

    def click_logo_yandex(self):
        self.wait_load_any_element(locator=self.logo_yandex)
        self.driver.find_element(*self.logo_yandex).click()
        self.switch_to_windows()
        self.wait_load_any_element(locator=self.page_yandex)
