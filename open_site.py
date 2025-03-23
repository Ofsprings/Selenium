from selenium import webdriver

# Инициализация драйвера
driver = webdriver.Chrome()  # или webdriver.Firefox()

# Открыть сайт
driver.get("https://www.google.com")

# Проверить заголовок страницы
assert "Google" in driver.title

# Закрыть браузер
driver.quit()