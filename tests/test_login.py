from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.locators import Locators


class TestLogin():

    def test_login_to_account_button(self, driver):
        driver.find_element(*Locators.LK).click()
        driver.find_element(*Locators.EMAIL).send_keys('Ermakova_Polina_1@ya.ru')
        driver.find_element(*Locators.PASSWORD).send_keys('111111')
        driver.find_element(*Locators.LOGIN_BUTTON).click()

    def test_login_personal_account_button(self, driver):
        driver.find_element(By.XPATH, '//button[contains(text(),"Войти в аккаунт")]').click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.ENTRY))
        driver.find_element(*Locators.EMAIL).send_keys('Ermakova_Polina_1@ya.ru')
        driver.find_element(*Locators.PASSWORD).send_keys('111111')
        driver.find_element(*Locators.LOGIN_BUTTON).click()

    def test_login_in_registration_form(self, driver):
        driver.find_element(*Locators.LK).click()
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, '//h2[contains(text(),"Регистрация")]')))
        driver.find_element(By.XPATH, '//a[contains(text(),"Войти")]').click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.ENTRY))
        driver.find_element(*Locators.EMAIL).send_keys('Ermakova_Polina_1@ya.ru')
        driver.find_element(*Locators.PASSWORD).send_keys('111111')
        driver.find_element(*Locators.LOGIN_BUTTON).click()

    def test_login_in_password_recovery_form(self, driver):
        driver.find_element(*Locators.LK).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            Locators.ENTRY))
        driver.find_element(By.XPATH, '//a[contains(text(),"Восстановить пароль")]').click()
        driver.find_element(By.XPATH, '//a[contains(text(),"Войти")]').click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.ENTRY))
        driver.find_element(*Locators.EMAIL).send_keys('Ermakova_Polina_1@ya.ru')
        driver.find_element(*Locators.PASSWORD).send_keys('111111')
        driver.find_element(*Locators.LOGIN_BUTTON).click()

