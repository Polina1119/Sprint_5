from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.locators import LoginPageLocators as Login
from tests.locators import ProfilePageLocators as Profile


class TestLogout():

    def test_logout(self, login):
        driver = login
        driver.find_element(*Login.LK).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Profile.PROFILE))
        driver.find_element(*Profile.LOGOUT).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Login.ENTRY))

        assert driver.find_element(*Login.ENTRY).text == 'Вход'

