from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# Функция для вычисления значения выражения
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

# Настройка WebDriver (например, для Chrome)
browser = webdriver.Chrome()

try:
    # Открытие страницы
    browser.get("http://suninjuly.github.io/redirect_accept.html")

    # Нажатие на кнопку, которая открывает новую вкладку
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()

    # Переключение на новую вкладку
    new_window = browser.window_handles[1]  # Индекс 1 указывает на новую вкладку
    browser.switch_to.window(new_window)

    # Решение капчи
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    result = calc(x)

    # Ввод результата в текстовое поле
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(result)

    # Нажатие кнопки "Submit"
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

    # Ждем несколько секунд, чтобы увидеть результат
    time.sleep(10)

finally:
    # Закрываем браузер
    browser.quit()
