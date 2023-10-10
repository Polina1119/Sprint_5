from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import random
from tests.locators import RegPageLocators as Reg
from tests.locators import LoginPageLocators as Login


class TestRegistration():

    def test_registration_password_6_symbols(self, driver):
        driver.find_element(*Login.LK).click()
        driver.find_element(*Login.REG_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Reg.REGISTRATION))
        number = random.randint(1, 999)
        driver.find_element(*Reg.NAME).send_keys(f'Ermakova_Polina_{number}')
        driver.find_element(*Reg.EMAIL).send_keys(f'Ermakova_Polina_1{number}@ya.ru')
        driver.find_element(*Reg.PASSWORD).send_keys(f'{random.randint(000000, 999999)}')
        driver.find_element(*Reg.REG_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Login.ENTRY))

        assert driver.find_element(*Login.ENTRY).text == 'Вход'

    def test_registration_password_5_symbols(self, driver):
        driver.find_element(*Login.LK).click()
        driver.find_element(*Login.REG_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Reg.REGISTRATION))
        number = random.randint(1, 999)
        driver.find_element(*Reg.NAME).send_keys(f'Ermakova_Polina_{number}')
        driver.find_element(*Reg.EMAIL).send_keys(f'Ermakova_Polina_1{number}@ya.ru')
        driver.find_element(*Reg.PASSWORD).send_keys(f'{random.randint(00000, 99999)}')
        driver.find_element(*Reg.REG_BUTTON).click()

        assert driver.find_element(*Reg.INCORRECT_PASSWORD).text == 'Некорректный пароль'

