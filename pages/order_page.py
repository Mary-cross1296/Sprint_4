import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class OrderPageScooter:

    button_order_up = [By.CLASS_NAME, 'Button_Button__ra12g']
    button_order_middle = [By.CLASS_NAME, 'Button_Button__ra12g Button_Middle__1CSJM']
    def __init__(self, driver):
        self.driver = driver

    def scroll_end_main_page(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def wait_button_order_up(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(*self.button_order_up))

    def wait_button_order_middle(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(*self.button_order_middle))

    def click_button_order_up(self):
        self.driver.find_element(*self.button_order_up).click()

    def click_button_order_middle(self):
        self.driver.find_element(*self.button_order_middle).click()

    def get_url_page(self):
        self.driver.current_url


