import allure

class TestOrderPage:

    @allure.title('Проверка перехода по логотипу "Самокат"')
    def test_logo_scoooter(self, driver, order_page, url):
        driver.get(url.main_page_url)
        order_page.wait_load_any_element(locator=order_page.button_order_up)
        order_page.click_button_order_up()
        order_page.click_logo_scooter()
        order_page.scroll_end_page()
        assert order_page.get_text_any_element(locator=order_page.title_questions_important)

    @allure.title('Проверка перехода по кнопке "Заказать" вверху страницы')
    def test_button_order_up(self, driver, order_page, url):
        driver.get(url.main_page_url)
        order_page.go_order_section_up()
        order_page.wait_load_any_element(locator=order_page.title_order_page)
        assert order_page.get_text_any_element(locator=order_page.title_order_page) == "Для кого самокат"

    @allure.title('Проверка перехода по кнопке "Заказать" в середине страницы')
    def test_button_order_middle(self, driver, order_page, url):
        driver.get(url.main_page_url)
        order_page.scroll_end_page()
        order_page.go_order_section_middle()
        order_page.wait_load_any_element(locator=order_page.title_order_page)
        assert order_page.get_text_any_element(locator=order_page.title_order_page) == "Для кого самокат"

    @allure.title('Проверка оформления заказа (с комментараем для курьера, цвет самоката - черный)')
    def test_make_order_with_comment_and_color1(self, driver, order_page, new_user, url):
        driver.get(url.main_page_url)
        order_page.wait_load_any_element(locator=order_page.button_order_up)
        order_page.click_button_order_up()
        order_page.wait_load_any_element(locator=order_page.title_order_page)
        order_page.data_filling_part_1(new_user.name, new_user.last_name, new_user.address, new_user.phone)
        order_page.continue_make_order()
        order_page.data_filling_part_2_1(new_user.delivery_date_rand, new_user.comment)
        order_page.click_make_order()
        assert order_page.confirmation_order() == "Отменить заказ"

    @allure.title('Проверка оформления заказа (без комментария для курьера, цвет самоката - серый)')
    def test_make_order_no_comment_and_color2(self, driver, order_page, new_user, url):
        driver.get(url.main_page_url)
        order_page.scroll_end_page()
        order_page.click_button_order_middle()
        order_page.wait_load_any_element(locator=order_page.title_order_page)
        order_page.data_filling_part_1(new_user.name, new_user.last_name, new_user.address, new_user.phone)
        order_page.continue_make_order()
        order_page.data_filling_part_2_2(new_user.delivery_date_rand)
        order_page.click_make_order()
        assert order_page.confirmation_order() == "Отменить заказ"