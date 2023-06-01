from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from auth_helper import User

class OrderPageScooter:

    def __init__(self, driver):
        self.driver = driver

    button_order_up = [By.CLASS_NAME, 'Button_Button__ra12g']
    button_order_middle = [By.XPATH, './/button[@class = "Button_Button__ra12g Button_Middle__1CSJM"]']
    title_order_page = [By.CLASS_NAME, 'Order_Header__BZXOb']
    name = [By.XPATH, './/input[@placeholder = "* Имя"]']
    last_name = [By.XPATH, './/input[@placeholder = "* Фамилия"]']
    address = [By.XPATH, './/input[@placeholder = "* Адрес: куда привезти заказ"]']
    metro_station = [By.XPATH, './/input[@placeholder = "* Станция метро"]']
    metro_station_list = [By.XPATH, './/ul/li/button[@value = "50"]']
    phone_number = [By.XPATH, './/input[@placeholder = "* Телефон: на него позвонит курьер"]']
    button_next = [By.XPATH, './/div[@class = "Order_NextButton__1_rCA"]/button[@class = "Button_Button__ra12g Button_Middle__1CSJM"]']
    delivery_date = [By.XPATH, './/input[@placeholder = "* Когда привезти самокат"]']
    date_in_calendar = [By.XPATH, './/div[@tabindex = "0"]']
    rental_period = [By.XPATH, './/span[@class = "Dropdown-arrow"]']
    days_5 = [By.XPATH, './/div[@class = "Dropdown-menu"]/div[text() ="пятеро суток"]']
    open_area = [By.XPATH, './/div[@class = "Header_Header__214zg"]']
    black_color = [By.ID, 'black']
    grey_color = [By.ID, 'grey']
    comment_courier = [By.XPATH, './/input[@placeholder = "Комментарий для курьера"]']
    button_order = [By.XPATH, './/button[@class = "Button_Button__ra12g Button_Middle__1CSJM"]']
    button_checkout_order_yes = [By.XPATH, './/button[text() = "Да"]']
    button_checkout_status = [By.XPATH, './/button[text() = "Посмотреть статус"]']
    button_cancel_order = [By.XPATH, './/button[text() = "Отменить заказ"]']
    logo_scooter = [By.XPATH, './/img[@alt ="Scooter"]']

    def scroll_end_main_page(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def wait_button_order_up(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((self.button_order_up)))

    def wait_button_order_middle(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((self.button_order_middle)))

    def wait_title_order_page(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((self.title_order_page)))

    def click_button_order_up(self):
        self.driver.find_element(*self.button_order_up).click()

    def click_button_order_middle(self):
        self.driver.find_element(*self.button_order_middle).click()

    def get_page_url(self):
        return self.driver.current_url

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

    def click_make_order(self):
        self.driver.find_element(*self.button_order).click()

    def confirmation_order(self):
        self.driver.find_element(*self.button_checkout_order_yes).click()
        self.driver.find_element(*self.button_checkout_status).click()
        return self.driver.find_element(*self.button_cancel_order).text

    def click_logo_scooter(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located
                                            ((self.logo_scooter)))
        self.driver.find_element(*self.logo_scooter).click()
