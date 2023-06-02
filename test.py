import pytest
import allure
from selenium.webdriver.common.by import By

class TestMainPage:

    @allure.title('Проверка перехода по логотипу Яндекса')
    def test_click_logo_yandex(self, driver, main_page, url):
        driver.get(url.main_page_url)
        main_page.click_logo_yandex()
        #assert main_page.get == url.yandex_page_url
        #assert main_page.get_page_url() == url.yandex_page_url
        assert main_page.get_text_any_element(locator=main_page.page_yandex) == "Найти"

