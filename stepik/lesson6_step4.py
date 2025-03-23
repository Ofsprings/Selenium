from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполняем поле "First name"
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")

    # Заполняем поле "Last name"
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")

    # Заполняем поле "City"
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")

    # Заполняем поле "Country"
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")

    # Нажимаем кнопку "Submit"
    submit_button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    submit_button.click()

finally:
    # Успеваем скопировать код за 30 секунд
    time.sleep(30)
    # Закрываем браузер после всех манипуляций
    browser.quit()

# Не забываем оставить пустую строку в конце файла