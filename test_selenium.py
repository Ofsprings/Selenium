from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализация драйвера
driver = webdriver.Chrome()

# Открытие сайта
driver.get("https://www.example.com")

# Проверка заголовка страницы
assert "Example Domain" in driver.title

# Закрытие браузера
driver.quit()