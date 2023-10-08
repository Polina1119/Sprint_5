from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.locators import Locators


class TestConstructor():

    def test_constructor_button(self, login):
        driver = login
        driver.find_element(*Locators.CONSTRUCTOR).click()

        assert driver.find_element(*Locators.BURGER).text == 'Соберите бургер'

    def test_constructor_logo_button(self, login):
        driver = login
        driver.find_element(*Locators.STELLAR_BURGERS).click()

        assert driver.find_element(*Locators.BURGER).text == 'Соберите бургер'

    def test_sauces(self, login):
        driver = login
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.BURGER))
        driver.find_element(*Locators.SAUCE).click()

        assert driver.find_element(*Locators.SAUCES).text == "Соусы"

    def test_buns(self, login):
        driver = login
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.BURGER))

        assert driver.find_element(*Locators.BUNS).text == 'Булки'

    def test_fillings(self, login):
        driver = login
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.BURGER))
        driver.find_element(*Locators.FILLING).click()

        assert driver.find_element(*Locators.FILLINGS).text == 'Начинки'

