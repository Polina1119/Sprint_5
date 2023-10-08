from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import random
from tests.locators import Locators


class TestRegistration():

    def test_registration_password_6_symbols(self, driver):
        driver.find_element(*Locators.LK).click()
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, '//h2[contains(text(),"Регистрация")]')))
        number = random.randint(1, 999)
        driver.find_element(By.XPATH, '//div/form/fieldset[1]/div/div/input').send_keys(f'Ermakova_Polina_{number}')
        driver.find_element(By.XPATH, '//div/form/fieldset[2]/div/div/input').send_keys(f'Ermakova_Polina_1{number}@ya.ru')
        driver.find_element(*Locators.PASSWORD).send_keys(f'{random.randint(000000, 999999)}')
        driver.find_element(*Locators.REG_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.ENTRY))

        assert driver.find_element(*Locators.ENTRY).text == 'Вход'

    def test_registration_password_5_symbols(self, driver):
        driver.find_element(*Locators.LK).click()
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, '//h2[contains(text(),"Регистрация")]')))
        number = random.randint(1, 999)
        driver.find_element(By.XPATH, '//div/form/fieldset[1]/div/div/input').send_keys(f'Ermakova_Polina_{number}')
        driver.find_element(By.XPATH, '//div/form/fieldset[2]/div/div/input').send_keys(f'Ermakova_Polina_1{number}@ya.ru')
        driver.find_element(*Locators.PASSWORD).send_keys(f'{random.randint(00000, 99999)}')
        driver.find_element(*Locators.REG_BUTTON).click()

        assert driver.find_element(By.XPATH, '//p[contains(text(),"Некорректный пароль")]').text == 'Некорректный пароль'

