from selenium.webdriver.common.by import By


class Locators():
    REG_BUTTON = (By.XPATH, '//button[contains(text(),"Зарегистрироваться")]') # кнопка Зарегистрироваться
    LK = (By.XPATH, '//p[contains(text(),"Личный Кабинет")]') # кнопка Личный кабинет
    LOGIN_BUTTON = (By.XPATH, '//button[contains(text(),"Войти")]') # кнопка Войти
    EMAIL = (By.TAG_NAME, 'input') # поле ввода email
    PASSWORD = (By.NAME, 'Пароль') # поле ввода пароля
    REGISTER_BUTTON = (By.XPATH, '//a[contains(text(),"Зарегистрироваться")]') # ссылка на форму регистрации
    ENTRY = (By.XPATH, '//h2[contains(text(),"Вход")]') # заголовок Вход
    PROFILE = (By.XPATH, '//a[contains(text(),"Профиль")]') # раздел Профиль
    BURGER = (By.XPATH, '//h1[contains(text(),"Соберите бургер")]') # заголовок Соберите бургер
    LOGIN_TO_ACCOUNT = (By.XPATH, '//button[contains(text(),"Войти в аккаунт")]') # кнопка Войти в аккаунт
    REGISTRATION = (By.XPATH, '//h2[contains(text(),"Регистрация")]') # заголовок Регистрация
    LOGIN = (By.XPATH, '//a[contains(text(),"Войти")]') # кнопка Войти в форме регистрации
    RECOVERY_PASSWORD = (By.XPATH, '//a[contains(text(),"Восстановить пароль")]') #кнопка Восстановить пароль
    LOGOUT = (By.XPATH, '//button[contains(text(),"Выход")]') #кнопка Выход
    CONSTRUCTOR = (By.XPATH, '//p[contains(text(),"Конструктор")]') #кнопка Конструктор
    STELLAR_BURGERS = (By.XPATH, '//header/nav/div/a/*') # заголовок Stellar burgers
    SAUCE = (By.XPATH, '//span[contains(text(),"Соусы")]') # раздел Соусы
    SAUCES = (By.XPATH, '//h2[contains(text(),"Соусы")]') # заголовок Соусы
    BUNS = (By.XPATH, '//h2[contains(text(),"Булки")]') # заголовок Булки
    FILLING = (By.XPATH, '//span[contains(text(),"Начинки")]') # раздел Начинки
    FILLINGS = (By.XPATH, '//h2[contains(text(),"Начинки")]') # заголовок Начинки


