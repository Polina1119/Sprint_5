from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.locators import Locators


class TestLogout():

    def test_logout(self, login):
        driver = login
        driver.find_element(*Locators.LK).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.PROFILE))
        driver.find_element(*Locators.LOGOUT).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.ENTRY))

        assert driver.find_element(*Locators.ENTRY).text == 'Вход'

