from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.locators import Locators


class TestPersonalAccount():

    def test_go_to_personal_account(self, login):
        driver = login
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.BURGER))
        driver.find_element(*Locators.LK).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.PROFILE))

        assert driver.find_element(*Locators.PROFILE).text == 'Профиль'

