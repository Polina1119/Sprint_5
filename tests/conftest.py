import pytest
from selenium import webdriver
from tests.data import Data
from tests.locators import LoginPageLocators as Login


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get(Data.url)

    yield driver
    driver.quit()

@pytest.fixture
def login(driver):
    driver.find_element(*Login.LK).click()
    driver.find_element(*Login.EMAIL).send_keys(Data.email)
    driver.find_element(*Login.PASSWORD).send_keys(Data.password)
    driver.find_element(*Login.LOGIN_BUTTON).click()

    return driver



