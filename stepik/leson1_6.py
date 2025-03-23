# from selenium import webdriver
# from selenium.webdriver.common.by import By

# print("Запуск браузера...")
# browser = webdriver.Chrome()
# print("Открытие страницы...")
# browser.get("http://suninjuly.github.io/simple_form_find_task.html")
# print("Поиск кнопки...")
# button = browser.find_element(By.ID, "submit_button")
# print("Кнопка найдена.")

# # закрываем браузер после всех манипуляций
# browser.quit()
# print("закрываем браузер после всех манипуляций")

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.ID, "submit_button")
    button.click()

finally:
    # закрываем браузер после всех манипуляций
    browser.close()