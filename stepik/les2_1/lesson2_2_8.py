from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# Настройка WebDriver (например, для Chrome)
browser = webdriver.Chrome()

try:
    # Открытие страницы
    browser.get("http://suninjuly.github.io/file_input.html")

    # Заполнение текстовых полей
    first_name = browser.find_element(By.NAME, "firstname")
    first_name.send_keys("Иван")

    last_name = browser.find_element(By.NAME, "lastname")
    last_name.send_keys("Иванов")

    email = browser.find_element(By.NAME, "email")
    email.send_keys("ivan@example.com")

    # Загрузка файла
    current_dir = os.path.abspath(os.path.dirname(__file__))  # Получаем путь к текущей директории
    file_path = os.path.join(current_dir, "file.txt")  # Создаем путь к файлу
    file_input = browser.find_element(By.ID, "file")
    file_input.send_keys(file_path)

    # Нажатие кнопки "Submit"
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

    # Ждем несколько секунд, чтобы увидеть результат
    time.sleep(10)

finally:
    # Закрываем браузер
    browser.quit()