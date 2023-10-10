from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.data import Data
from tests.locators import LoginPageLocators as Login
from tests.locators import ProfilePageLocators as Profile
from tests.locators import ConstrPageLocators as Constructor
from tests.locators import RegPageLocators as Reg


class TestLogin():

    def test_login_to_account_button(self, driver):
        driver.find_element(*Login.LK).click()
        driver.find_element(*Login.EMAIL).send_keys(Data.email)
        driver.find_element(*Login.PASSWORD).send_keys(Data.password)
        driver.find_element(*Login.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Constructor.BURGER))
        driver.find_element(*Login.LK).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Profile.PROFILE))

        assert driver.find_element(*Profile.EMAIL).get_attribute('value') == Data.email

    def test_login_personal_account_button(self, driver):
        driver.find_element(*Login.LOGIN_TO_ACCOUNT).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Login.ENTRY))
        driver.find_element(*Login.EMAIL).send_keys(Data.email)
        driver.find_element(*Login.PASSWORD).send_keys(Data.password)
        driver.find_element(*Login.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Constructor.BURGER))
        driver.find_element(*Login.LK).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Profile.PROFILE))

        assert driver.find_element(*Profile.EMAIL).get_attribute('value') == Data.email

    def test_login_in_registration_form(self, driver):
        driver.find_element(*Login.LK).click()
        driver.find_element(*Login.REG_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Reg.REGISTRATION))
        driver.find_element(*Reg.LOGIN).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Login.ENTRY))
        driver.find_element(*Login.EMAIL).send_keys(Data.email)
        driver.find_element(*Login.PASSWORD).send_keys(Data.password)
        driver.find_element(*Login.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Constructor.BURGER))
        driver.find_element(*Login.LK).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Profile.PROFILE))

        assert driver.find_element(*Profile.EMAIL).get_attribute('value') == Data.email

    def test_login_in_password_recovery_form(self, driver):
        driver.find_element(*Login.LK).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Login.ENTRY))
        driver.find_element(*Login.RECOVERY_PASSWORD).click()
        driver.find_element(*Reg.LOGIN).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Login.ENTRY))
        driver.find_element(*Login.EMAIL).send_keys(Data.email)
        driver.find_element(*Login.PASSWORD).send_keys(Data.password)
        driver.find_element(*Login.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Constructor.BURGER))
        driver.find_element(*Login.LK).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Profile.PROFILE))

        assert driver.find_element(*Profile.EMAIL).get_attribute('value') == Data.email


