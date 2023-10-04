from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.locators import Locators


class TestConstructor():

    def test_constructor_button(self, login):
        driver = login
        driver.find_element(By.XPATH, '//p[contains(text(),"Конструктор")]').click()

        assert driver.find_element(*Locators.BURGER).text == 'Соберите бургер'

    def test_constructor_logo_button(self, login):
        driver = login
        driver.find_element(By.XPATH, '//header/nav/div/a/*').click()

        assert driver.find_element(*Locators.BURGER).text == 'Соберите бургер'

    def test_sauces(self, login):
        driver = login
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.BURGER))
        driver.find_element(By.XPATH, '//span[contains(text(),"Соусы")]').click()

        assert driver.find_element(By.XPATH, '//h2[contains(text(),"Булки")]').text == "Булки"

    def test_buns(self, login):
        driver = login
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.BURGER))

        assert driver.find_element(By.XPATH, '//h2[contains(text(),"Булки")]').text == 'Булки'

    def test_fillings(self, login):
        driver = login
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.BURGER))
        driver.find_element(By.XPATH, '//span[contains(text(),"Начинки")]').click()

        assert driver.find_element(By.XPATH, '//h2[contains(text(),"Начинки")]').text == 'Начинки'

