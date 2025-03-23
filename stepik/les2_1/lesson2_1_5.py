from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

# Функция для вычисления значения
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

# Инициализация браузера
browser = webdriver.Chrome()

try:
    # Открытие страницы
    browser.get("https://suninjuly.github.io/math.html")

    # Считывание значения x
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text

    # Вычисление значения функции
    y = calc(x)

    # Ввод ответа в текстовое поле
    answer_input = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer_input.send_keys(y)

    # Отметка checkbox "I'm the robot"
    checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox.click()

    # Выбор radiobutton "Robots rule!"
    radiobutton = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radiobutton.click()

    # Нажатие на кнопку Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

    # Ожидание для визуальной проверки результата
    time.sleep(10)

finally:
    # Закрытие браузера
    browser.quit()