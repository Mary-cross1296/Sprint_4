from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from auth_helper import User

class OrderPageScooter(BasePage):

    def __init__(self, driver):
        self.driver = driver

    button_order_up = [By.XPATH, './/button[text() = "Статус заказа"]/preceding-sibling::button[text()="Заказать"]']
    button_order_middle = [By.XPATH, './/div[text()="Как это работает"]/following::div/div/button[text()="Заказать"]']
    title_order_page = [By.CLASS_NAME, 'Order_Header__BZXOb']
    name = [By.XPATH, './/input[@placeholder = "* Имя"]']
    last_name = [By.XPATH, './/input[@placeholder = "* Фамилия"]']
    address = [By.XPATH, './/input[@placeholder = "* Адрес: куда привезти заказ"]']
    metro_station = [By.XPATH, './/input[@placeholder = "* Станция метро"]']
    metro_station_list = [By.XPATH, './/ul/li/button[@value = "50"]']
    phone_number = [By.XPATH, './/input[@placeholder = "* Телефон: на него позвонит курьер"]']
    button_next = [By.XPATH, './/button[text() = "Далее"]']
    delivery_date = [By.XPATH, './/input[@placeholder = "* Когда привезти самокат"]']
    date_in_calendar = [By.XPATH, './/div[@tabindex = "0"]']
    rental_period = [By.XPATH, './/span[@class = "Dropdown-arrow"]']
    days_5 = [By.XPATH, './/div[@class = "Dropdown-menu"]/div[text() ="пятеро суток"]']
    black_color = [By.ID, 'black']
    grey_color = [By.ID, 'grey']
    comment_courier = [By.XPATH, './/input[@placeholder = "Комментарий для курьера"]']
    button_order = [By.XPATH, './/button[text() = "Назад"]/following::button[text() = "Заказать"]']
    button_checkout_order_yes = [By.XPATH, './/button[text() = "Да"]']
    button_checkout_status = [By.XPATH, './/button[text() = "Посмотреть статус"]']
    button_cancel_order = [By.XPATH, './/button[text() = "Отменить заказ"]']
    logo_scooter = [By.XPATH, './/img[@alt ="Scooter"]']

    def click_button_order_up(self):
        self.driver.find_element(*self.button_order_up).click()

    def click_button_order_middle(self):
        self.driver.find_element(*self.button_order_middle).click()

    def go_order_section_up(self):
        self.wait_load_any_element(locator=self.button_order_up)
        self.click_button_order_up()

    def go_order_section_middle(self):
        self.wait_load_any_element(locator=self.button_order_middle)
        self.click_button_order_middle()

    def enter_name(self, user_name):
        self.driver.find_element(*self.name).send_keys(user_name)

    def enter_last_name(self, user_last_name):
        self.driver.find_element(*self.last_name).send_keys(user_last_name)

    def enter_address_name(self, user_address):
        self.driver.find_element(*self.address).send_keys(user_address)

    def enter_metro_station(self):
        self.driver.find_element(*self.metro_station).click()
        self.driver.find_element(*self.metro_station_list).click()

    def enter_phone_number(self,user_phone_number):
        self.driver.find_element(*self.phone_number).send_keys(user_phone_number)

    def data_filling_part_1(self, user_name, user_last_name, user_address, user_phone_number):
        self.enter_name(user_name)
        self.enter_last_name(user_last_name)
        self.enter_address_name(user_address)
        self.enter_metro_station()
        self.enter_phone_number(user_phone_number)

    def continue_make_order(self):
        self.driver.find_element(*self.button_next).click()

    def enter_delivery_date(self, user_delivery_date):
        self.driver.find_element(*self.delivery_date).send_keys(user_delivery_date)

    def enter_rental_period(self):
        self.driver.find_element(*self.rental_period).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((self.days_5)))
        self.driver.find_element(*self.days_5).click()

    def choose_color1_scooter(self):
        self.driver.find_element(*self.black_color).click()

    def choose_color2_scooter(self):
        self.driver.find_element(*self.grey_color).click()

    def enter_comment_courier(self, user_comment):
        self.driver.find_element(*self.comment_courier).send_keys(user_comment)

    def data_filling_part_2_1(self, user_delivery_date, user_comment):
        self.enter_delivery_date(user_delivery_date)
        self.enter_rental_period()
        self.choose_color1_scooter()
        self.enter_comment_courier(user_comment)

    def data_filling_part_2_2(self, user_delivery_date):
        self.enter_delivery_date(user_delivery_date)
        self.enter_rental_period()
        self.choose_color1_scooter()

    def click_make_order(self):
        self.driver.find_element(*self.button_order).click()

    def confirmation_order(self):
        self.wait_load_any_element(locator=self.button_checkout_order_yes)
        self.driver.find_element(*self.button_checkout_order_yes).click()
        self.wait_load_any_element(locator=self.button_checkout_status)
        self.driver.find_element(*self.button_checkout_status).click()
        self.wait_load_any_element(locator=self.button_cancel_order)
        return self.get_text_any_element(locator=self.button_cancel_order)

    def click_logo_scooter(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located
                                            ((self.logo_scooter)))
        self.driver.find_element(*self.logo_scooter).click()
