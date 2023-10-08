import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from tests.data import Data
from tests.locators import Locators


@pytest.fixture
def driver():
    option = Options()
    option.add_argument("--window-size=1200,600")
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(options=option, service=service)
    browser.get(Data.url)

    yield browser
    browser.quit()

@pytest.fixture
def login(driver):
    driver.find_element(*Locators.LK).click()
    driver.find_element(*Locators.EMAIL).send_keys(Data.email)
    driver.find_element(*Locators.PASSWORD).send_keys(Data.password)
    driver.find_element(*Locators.LOGIN_BUTTON).click()

    return driver



