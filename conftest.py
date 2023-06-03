import pytest
import allure
from selenium import webdriver

from auth_helper import User
from pages.main_page import MainPageScooter
from pages.order_page import OrderPageScooter
from urls import Urls

@pytest.fixture
def driver():
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=options)
    driver.set_window_size(1200, 1500)
    yield driver
    driver.quit()

@pytest.fixture
def main_page(driver):
    mp = MainPageScooter(driver)
    return mp

@pytest.fixture
def order_page(driver):
    op = OrderPageScooter(driver)
    return op

@pytest.fixture
def new_user():
    nu = User()
    return nu

@pytest.fixture
def url():
    url_page = Urls()
    return url_page
