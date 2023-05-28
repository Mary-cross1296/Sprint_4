import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from auth_helper import User

class OrderPageScooter:

    button_order_up = [By.CLASS_NAME, 'Button_Button__ra12g']
    button_order_middle = [By.XPATH, './/button[@class = "Button_Button__ra12g Button_Middle__1CSJM"]']
    title_order_page = [By.CLASS_NAME, 'Order_Header__BZXOb']
    name = [By.CLASS_NAME, 'Input_Input__1iN_Z Input_Error__1Tx5d Input_Responsible__1jDKN']

    def __init__(self, driver):
        self.driver = driver

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

class TestOrderPage:

    def test_button_order_up(self, driver):
        order_page = OrderPageScooter(driver)
        driver.get('https://qa-scooter.praktikum-services.ru/')
        order_page.wait_button_order_up()
        order_page.click_button_order_up()
        order_page.wait_title_order_page()
        assert order_page.get_page_url() == 'https://qa-scooter.praktikum-services.ru/order'

    def test_button_order_middle(self, driver):
        order_page = OrderPageScooter(driver)
        driver.get('https://qa-scooter.praktikum-services.ru/')
        order_page.scroll_end_main_page()
        order_page.wait_button_order_middle()
        order_page.click_button_order_middle()
        order_page.wait_title_order_page()
        assert order_page.get_page_url() == 'https://qa-scooter.praktikum-services.ru/order'

    def test_make_order(self,driver):
        new_user = User()
        order_page = OrderPageScooter(driver)
        driver.get('https://qa-scooter.praktikum-services.ru/')
        order_page.wait_button_order_up()
        order_page.click_button_order_up()
        order_page.wait_title_order_page()






