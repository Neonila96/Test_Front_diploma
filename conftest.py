import time
import pytest
import requests
from selenium import webdriver
from home_page import HomePage
from login_page import LoginPage

@pytest.fixture(scope="class")
def init_driver(request):
    # Инициализация драйвера

    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # driver = webdriver.Chrome(options=options)

    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver

    # Инициализация страницы
    login_page = LoginPage(driver)
    home_page = HomePage(driver)

    # Открытие страницы
    login_page.open_login_page()

    # Логинимся
    login_page.login_user()
    time.sleep(10)

    # Заходим на сервер диплом
    home_page.clic_to_server_diplow()
    time.sleep(5)
    # Переходим в канал "6"
    home_page.clic_to_channel()
    time.sleep(5)
    yield driver
    driver.quit()


@pytest.fixture(scope="class")
def base_url():
    return 'https://discord.com/login'


@pytest.fixture(scope="class")
def base_url():
    return 'https://discord.com/login'


@pytest.fixture(scope="class")
def base_url():
    return 'https://discord.com/login'






