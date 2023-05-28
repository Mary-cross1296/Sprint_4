import pytest
#from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=options)
    driver.set_window_size(1200, 1500)
    yield driver
    driver.quit()

