from selenium import webdriver
from selenium.webdriver.common.by import By

# Настройка WebDriver (например, для Chrome)
browser = webdriver.Chrome()

try:
    # Открытие страницы
    browser.get("http://suninjuly.github.io/math.html")

    # Поиск элемента radiobutton по ID
    people_radio = browser.find_element(By.ID, "peopleRule")

    # Получение значения атрибута 'checked'
    people_checked = people_radio.get_attribute("checked")

    # Проверка, что атрибут 'checked' равен "true"
    assert people_checked == "true", "People radio is not selected by default"

    # Поиск другого radiobutton по ID
    robots_radio = browser.find_element(By.ID, "robotsRule")

    # Получение значения атрибута 'checked'
    robots_checked = robots_radio.get_attribute("checked")

    # Проверка, что атрибут 'checked' отсутствует (равен None)
    assert robots_checked is None, "Robots radio should not be selected by default"

    # Пример проверки атрибута 'disabled' у кнопки
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    is_disabled = submit_button.get_attribute("disabled")

    # Проверка, что кнопка disabled
    assert is_disabled == "true", "Submit button should be disabled"

finally:
    # Закрытие браузера
    browser.quit()