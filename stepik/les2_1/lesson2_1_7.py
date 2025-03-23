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
    browser.get("http://suninjuly.github.io/get_attribute.html")

    # Находим элемент-картинку (сундук) и получаем значение атрибута valuex
    treasure_img = browser.find_element(By.ID, "treasure")
    x_value = treasure_img.get_attribute("valuex")

    # Вычисляем значение выражения
    result = calc(x_value)

    # Вводим результат в текстовое поле
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(result)

    # Отмечаем checkbox "I'm the robot"
    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()

    # Выбираем radiobutton "Robots rule!"
    robots_rule_radio = browser.find_element(By.ID, "robotsRule")
    robots_rule_radio.click()

    # Нажимаем на кнопку "Submit"
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

    # Ждем несколько секунд, чтобы увидеть результат
    time.sleep(10)

finally:
    # Закрываем браузер
    browser.quit()