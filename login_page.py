from base_page import BasePage
from selenium.webdriver.common.by import By
import time

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Локатор для кнопки "Вход"
    def login_user_button_locator(self):
        return By.XPATH, f'//button//div[text()="Вход"]'

    # Локатор для ввода логина
    def login_input_locator(self):
        return By.XPATH, f'//input[@id="uid_7"]'

    # Локатор для ввода пароля
    def password_input_locator(self):
        return By.XPATH, f'//input[@id="uid_9"]'

    # Метод для залогиниться
    def login_user(self):
        self.find_element(self.login_input_locator())
        self.send_keys(self.login_input_locator(), "neonila.zinova@icloud.com")
        self.find_element(self.password_input_locator())
        self.send_keys(self.password_input_locator(), "1809Vika")
        self.find_element(self.login_user_button_locator())
        time.sleep(5)
        self.click(self.login_user_button_locator())

    # Метод для открытия страницы
    def open_login_page(self):
        self.open_page()
