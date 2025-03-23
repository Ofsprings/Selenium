from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

# Инициализация драйвера
browser = webdriver.Chrome()

try:
    # Открываем страницу
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # Ожидаем, пока цена не станет $100
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # Нажимаем на кнопку "Book"
    book_button = browser.find_element(By.ID, "book")
    book_button.click()

    # Решаем математическую задачу
    # Находим значение x
    x_element = browser.find_element(By.ID, "input_value")
    x = int(x_element.text)

    # Вычисляем результат
    result = str(math.log(abs(12 * math.sin(x))))

    # Вводим ответ в поле
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(result)

    # Отправляем форму
    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()

    # Получаем результат из alert
    alert = browser.switch_to.alert
    alert_text = alert.text
    print("Код для ответа:", alert_text.split()[-1])
    alert.accept()

finally:
    # Закрываем браузер
    time.sleep(5)
    browser.quit()