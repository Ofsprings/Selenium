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
    browser.get("https://SunInJuly.github.io/execute_script.html")

    # Находим элемент с числом и получаем его значение
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text

    # Вычисляем значение выражения
    result = calc(x)

    # Находим текстовое поле и вводим результат
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(result)

    # Прокручиваем страницу вниз, чтобы элементы стали видимыми
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    # Выбираем checkbox "I'm the robot"
    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()

    # Переключаем radiobutton "Robots rule!"
    robots_rule_radio = browser.find_element(By.ID, "robotsRule")
    robots_rule_radio.click()

    # Нажимаем на кнопку "Submit"
    button.click()

    # Ждем несколько секунд, чтобы увидеть результат
    time.sleep(10)

finally:
    # Закрываем браузер
    browser.quit()