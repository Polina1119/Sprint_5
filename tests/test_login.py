from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.data import Data
from tests.locators import Locators


class TestLogin():

    def test_login_to_account_button(self, driver):
        driver.find_element(*Locators.LK).click()
        driver.find_element(*Locators.EMAIL).send_keys(Data.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Data.password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.BURGER))

        assert driver.find_element(*Locators.BURGER).text == 'Соберите бургер'

    def test_login_personal_account_button(self, driver):
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.ENTRY))
        driver.find_element(*Locators.EMAIL).send_keys(Data.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Data.password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.BURGER))

        assert driver.find_element(*Locators.BURGER).text == 'Соберите бургер'

    def test_login_in_registration_form(self, driver):
        driver.find_element(*Locators.LK).click()
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.REGISTRATION))
        driver.find_element(*Locators.LOGIN).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.ENTRY))
        driver.find_element(*Locators.EMAIL).send_keys(Data.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Data.password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.BURGER))

        assert driver.find_element(*Locators.BURGER).text == 'Соберите бургер'

    def test_login_in_password_recovery_form(self, driver):
        driver.find_element(*Locators.LK).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            Locators.ENTRY))
        driver.find_element(*Locators.RECOVERY_PASSWORD).click()
        driver.find_element(*Locators.LOGIN).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.ENTRY))
        driver.find_element(*Locators.EMAIL).send_keys(Data.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Data.password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.BURGER))

        assert driver.find_element(*Locators.BURGER).text == 'Соберите бургер'


