from selenium.webdriver.common.by import By


class Locators():
    REG_BUTTON = (By.XPATH, '//button[contains(text(),"Зарегистрироваться")]') # кнопка Зарегистрироваться
    LK = (By.XPATH, '//p[contains(text(),"Личный Кабинет")]') # кнопка Личный кабинет
    LOGIN_BUTTON = (By.XPATH, '//button[contains(text(),"Войти")]') # кнопка Войти
    EMAIL = (By.XPATH, '//div/form/fieldset/div/div/input') # поле ввода email
    PASSWORD = (By.NAME, 'Пароль') # поле ввода пароля
    REGISTER_BUTTON = (By.XPATH, '//a[contains(text(),"Зарегистрироваться")]') # ссылка на форму регистрации
    ENTRY = (By.XPATH, '//h2[contains(text(),"Вход")]') # заголовок
    PROFILE = (By.XPATH, '//a[contains(text(),"Профиль")]') # раздел Профиль
    BURGER = (By.XPATH, '//h1[contains(text(),"Соберите бургер")]') # заголовок

