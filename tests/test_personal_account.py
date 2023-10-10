from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.locators import LoginPageLocators as Login
from tests.locators import ConstrPageLocators as Constructor
from tests.locators import ProfilePageLocators as Profile

class TestPersonalAccount():

    def test_go_to_personal_account(self, login):
        driver = login
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Constructor.BURGER))
        driver.find_element(*Login.LK).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Profile.PROFILE))

        assert driver.find_element(*Profile.PROFILE).text == 'Профиль'

