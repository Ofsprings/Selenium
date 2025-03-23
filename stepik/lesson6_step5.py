import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Вычисляем текст ссылки
link_text = str(math.ceil(math.pow(math.pi, math.e) * 10000))

# Открываем страницу с зашифрованной ссылкой
link = "http://suninjuly.github.io/find_link_text"

try:
    # Инициализируем браузер
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим ссылку по тексту и кликаем по ней
    secret_link = browser.find_element(By.LINK_TEXT, link_text)
    secret_link.click()

    # Заполняем форму на новой странице
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")

    # Нажимаем кнопку "Submit"
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # Даем время для копирования кода
    time.sleep(30)
    # Закрываем браузер
    browser.quit()