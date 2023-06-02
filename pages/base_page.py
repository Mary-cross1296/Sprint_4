from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
class BasePage:

    title_questions_important = [By.XPATH, './/div[text() = "Вопросы о важном"]']

    def __init__(self, driver):
        self.driver = driver

    def scroll_end_page(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def wait_load_any_element(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))

    def switch_to_windows(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def get_page_url(self):
        return self.driver.current_url

    def get_text_any_element(self, locator):
        return self.driver.find_element(*locator).text
