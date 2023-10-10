from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.locators import ConstrPageLocators as Constructor


class TestConstructor():

    def test_constructor_button(self, login):
        driver = login
        driver.find_element(*Constructor.CONSTRUCTOR).click()

        assert driver.find_element(*Constructor.BURGER).text == 'Соберите бургер'

    def test_constructor_logo_button(self, login):
        driver = login
        driver.find_element(*Constructor.LOGO).click()

        assert driver.find_element(*Constructor.BURGER).text == 'Соберите бургер'

    def test_sauces(self, login):
        driver = login
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Constructor.BURGER))
        driver.find_element(*Constructor.SAUCE).click()

        assert driver.find_element(*Constructor.SAUCES).text == "Соусы"

    def test_buns(self, login):
        driver = login
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Constructor.BURGER))

        assert driver.find_element(*Constructor.BUNS).text == 'Булки'

    def test_fillings(self, login):
        driver = login
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Constructor.BURGER))
        driver.find_element(*Constructor.FILLING).click()

        assert driver.find_element(*Constructor.FILLINGS).text == 'Начинки'

