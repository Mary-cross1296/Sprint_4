import allure

class TestOrderPage:

    @allure.title('Проверка перехода по логотипу "Самокат"')
    def test_logo_scoooter(self, driver, order_page, url):
        driver.get(url.main_page_url)
        order_page.wait_button_order_up()
        order_page.click_button_order_up()
        order_page.click_logo_scooter()
        assert order_page.get_page_url() == 'https://qa-scooter.praktikum-services.ru/'

    @allure.title('Проверка перехода по кнопке "Заказать" вверху сраницы')
    def test_button_order_up(self, driver, order_page, url):
        driver.get(url.main_page_url)
        order_page.wait_button_order_up()
        order_page.click_button_order_up()
        order_page.wait_title_order_page()
        assert order_page.get_page_url() == 'https://qa-scooter.praktikum-services.ru/order'

    @allure.title('Проверка перехода по кнопке "Заказать" в середине страницы')
    def test_button_order_middle(self, driver, order_page, url):
        driver.get(url.main_page_url)
        order_page.scroll_end_main_page()
        order_page.wait_button_order_middle()
        order_page.click_button_order_middle()
        order_page.wait_title_order_page()
        assert order_page.get_page_url() == url.order_page_url

    @allure.title('Проверка оформления заказа (с комментараем для курьера, цвет самоката - черный)')
    def test_make_order_with_comment_and_color1(self, driver, order_page, new_user, url):
        driver.get(url.main_page_url)
        order_page.wait_button_order_up()
        order_page.click_button_order_up()
        order_page.wait_title_order_page()
        order_page.enter_name(new_user.name)
        order_page.enter_last_name(new_user.last_name)
        order_page.enter_address_name(new_user.address)
        order_page.enter_metro_station()
        order_page.enter_phone_number(new_user.phone)
        order_page.continue_make_order()
        order_page.enter_delivery_date(new_user.delivery_date_rand)
        order_page.enter_rental_period()
        order_page.choose_color1_scooter()
        order_page.enter_comment_courier(new_user.comment)
        order_page.click_make_order()
        assert order_page.confirmation_order() == "Отменить заказ"

    @allure.title('Проверка оформления заказа (без комментария для курьера, цвет самоката - серый)')
    def test_make_order_no_comment_and_color2(self, driver, order_page, new_user, url):
        driver.get(url.main_page_url)
        order_page.scroll_end_main_page()
        order_page.click_button_order_middle()
        order_page.wait_title_order_page()
        order_page.enter_name(new_user.name)
        order_page.enter_last_name(new_user.last_name)
        order_page.enter_address_name(new_user.address)
        order_page.enter_metro_station()
        order_page.enter_phone_number(new_user.phone)
        order_page.continue_make_order()
        order_page.enter_delivery_date(new_user.delivery_date_rand)
        order_page.enter_rental_period()
        order_page.choose_color2_scooter()
        order_page.click_make_order()
        assert order_page.confirmation_order() == "Отменить заказ"
