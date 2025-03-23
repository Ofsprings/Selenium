from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Настройка WebDriver (например, для Chrome)
browser = webdriver.Chrome()

try:
    # Открытие страницы
    browser.get("https://suninjuly.github.io/selects1.html")

    # Находим числа на странице и вычисляем их сумму
    num1 = browser.find_element(By.ID, "num1").text
    num2 = browser.find_element(By.ID, "num2").text
    total_sum = int(num1) + int(num2)

    # Выбираем в выпадающем списке значение, равное сумме
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(total_sum))  # Передаем строку, а не число

    # Нажимаем кнопку "Submit"
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

    # Ждем несколько секунд, чтобы увидеть результат
    time.sleep(10)

finally:
    # Закрываем браузер
    browser.quit()