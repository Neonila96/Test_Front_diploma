import time
import pytest
from home_page import HomePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Пишем какое сообщение хотим отправить
text = "Привет,привет"
text_mention = "Привет @BEE-diploma#7805 как ты?"
text_mention_non_exist_user = "Привет @васяпупкин как твое ничего?"

@pytest.mark.usefixtures("init_driver", "base_url")
class TestMessage:
    def test_send_message(self, base_url):
        # Инициализация страницы
        home_page = HomePage(self.driver)

        # Отправка сообщения
        home_page.send_message_in_channel(text)

        # Проверка, что сообщение отправилось в диалог
        message_send = home_page.is_message_send()
        assert message_send.count(text) == 1, "Сообщение не отправлено"


    def test_edit_message(self,base_url):
        # Инициализация страницы
        home_page = HomePage(self.driver)

        #Нажимаем редактировать сообщение
        home_page.edit_message()
        time.sleep(3)

        #Проверка, что новый текст с пометкой (изменено)
        new_message = home_page.is_message_send()
        assert new_message.count('изменено') == 1


    def test_add_reacrion(self, base_url):
        # Инициализация страницы
        home_page = HomePage(self.driver)

        # Поставить реакцию
        home_page.send_reactoin()
        time.sleep(3)
        # Проверка, что реакция появилась под сообщением
        assert home_page.is_reactoin_displayed().is_displayed() == True, "Реакция на сообщение отсутствует"


    def test_delete_reacrion(self, base_url):
        # Инициализация страницы
        home_page = HomePage(self.driver)

        # Удалить реакцию
        home_page.delete_reaction()

        # Проверка, что реакция исчезла
        assert WebDriverWait(self.driver, 5).until(
            EC.invisibility_of_element_located(home_page.reaction_locator()))


    def test_delete_message(self, base_url):
        # Инициализация страницы
        home_page = HomePage(self.driver)

        # Удалить сообщение
        home_page.delete_message()

        # Проверка, что сообщение удалилось
        assert WebDriverWait(self.driver, 5).until(
            EC.invisibility_of_element_located(home_page.form_message_locator()))


    def test_send_message_with_mention(self, base_url):
        # Инициализация страницы
        home_page = HomePage(self.driver)

        # Отправка сообщения
        home_page.send_message_in_channel(text_mention)
        time.sleep(3)

        # Проверка, что упомянутый пользователь существует
        role = home_page.is_mention_user_exists()
        assert role == "button"

        # Удалить сообщение
        home_page.delete_message()
        time.sleep(3)

@pytest.mark.usefixtures("init_driver", "base_url")
class TestNegative:
    def test_send_message_with_non_exist_user(self, base_url):
        # Инициализация страницы
        home_page = HomePage(self.driver)

        # Отправка сообщения
        home_page.send_message_in_channel(text_mention_non_exist_user)

        # Проверка, что упомянутый пользователь не существует
        assert home_page.is_mention_user_non_exists() == None

