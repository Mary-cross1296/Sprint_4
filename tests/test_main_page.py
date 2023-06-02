import pytest
import allure
from selenium.webdriver.common.by import By

class TestMainPage:

    @allure.title('Проверка наличия раздела "Вопросы о важном"')
    def test_section_questions(self, driver, main_page, url):
        driver.get(url.main_page_url)
        main_page.scroll_end_page()
        main_page.wait_load_any_element(locator=main_page.title_questions_important)
        title = main_page.get_text_any_element(locator=main_page.title_questions_important)
        assert title == 'Вопросы о важном'

    @pytest.mark.parametrize(
        'question, answer, expected_result',
        [
            [[By.ID, 'accordion__heading-0'],[By.ID, 'accordion__panel-0'], 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'],
            [[By.ID, 'accordion__heading-1'], [By.ID, 'accordion__panel-1'], 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'],
            [[By.ID, 'accordion__heading-2'], [By.ID, 'accordion__panel-2'], 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'],
            [[By.ID, 'accordion__heading-3'], [By.ID, 'accordion__panel-3'], 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'],
            [[By.ID, 'accordion__heading-4'], [By.ID, 'accordion__panel-4'], 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'],
            [[By.ID, 'accordion__heading-5'], [By.ID, 'accordion__panel-5'], 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'],
            [[By.ID, 'accordion__heading-6'], [By.ID, 'accordion__panel-6'], 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'],
            [[By.ID, 'accordion__heading-7'], [By.ID, 'accordion__panel-7'], 'Да, обязательно. Всем самокатов! И Москве, и Московской области.']
        ]
    )

    @allure.title('Проверка ответов на вопросы в разделе "Вопросы о важном"')
    def test_get_answer_to_question(self, driver, main_page, question, answer, expected_result, url):
        driver.get(url.main_page_url)
        main_page.scroll_end_page()
        answer_var = main_page.get_answer_to_question(question, answer)
        assert answer_var == expected_result

    @allure.title('Проверка перехода по логотипу Яндекса')
    def test_click_logo_yandex(self, driver, main_page, url):
        driver.get(url.main_page_url)
        main_page.click_logo_yandex()
        #assert main_page.get == url.yandex_page_url
        assert main_page.get_page_url() == url.yandex_page_url
