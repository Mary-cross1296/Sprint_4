from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage


class MainPageScooter(BasePage):

    def __init__(self, driver):
        self.driver = driver

    title_questions_important = [By.XPATH, './/div[text() = "Вопросы о важном"]']
    logo_yandex = [By.XPATH, './/div/a[@class ="Header_LogoYandex__3TSOI"]']
    page_yandex = [By.XPATH, './/button[text() ="Найти"]']

    #def scroll_end_main_page(self):
        #self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    #def wait_load_questions_important(self):
        #WebDriverWait(self.driver,3).until(expected_conditions.visibility_of_element_located
                                           #((self.title_questions_important)))

    def get_title_questions_important(self):
        return self.driver.find_element(*self.title_questions_important).text

    def get_answer_to_question(self, question, answer):
        #WebDriverWait(self.driver,3).until(expected_conditions.visibility_of_element_located((question)))
        self.wait_load_any_element(locator=question)
        self.driver.find_element(*question).click()
        #WebDriverWait(self.driver,3).until(expected_conditions.visibility_of_element_located((answer)))
        self.wait_load_any_element(locator=answer)
        return self.driver.find_element(*answer).text

    def click_logo_yandex(self):
        #WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located
                                            #((self.logo_yandex)))
        self.wait_load_any_element(locator=self.logo_yandex)
        self.driver.find_element(*self.logo_yandex).click()
        #self.driver.switch_to.window(self.driver.window_handles[1])
        self.switch_to_windows()
        #WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located
                                            #((self.page_yandex)))
        self.wait_load_any_element(locator=self.logo_yandex)

    def get_url_main_page(self):
        return self.driver.current_url
