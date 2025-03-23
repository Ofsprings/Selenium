from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time
import math

# Функция для вычисления значения выражения
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

# Настройка WebDriver (например, для Chrome)
browser = webdriver.Chrome()

try:
    # Открытие страницы
    browser.get("http://suninjuly.github.io/alert_accept.html")

    # Нажатие на кнопку, которая вызывает confirm
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()

    # Принятие confirm (нажатие "OK")
    confirm = browser.switch_to.alert
    confirm.accept()

    # Ждем загрузки новой страницы
    time.sleep(1)

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

    # Ждем появления alert с результатом
    time.sleep(1)  # Даем время для появления alert

    # Переключаемся на alert и копируем текст
    alert = Alert(browser)
    alert_text = alert.text
    print("Результат:", alert_text)  # Выводим результат в консоль
    alert.accept()  # Закрываем alert

finally:
    # Закрываем браузер
    browser.quit()