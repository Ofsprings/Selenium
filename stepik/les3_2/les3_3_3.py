import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


def test_registration1(browser):
    browser.get("http://suninjuly.github.io/registration1.html")

    # Заполняем обязательные поля
    browser.find_element(By.CSS_SELECTOR, ".first_block .first").send_keys("Ivan")
    browser.find_element(By.CSS_SELECTOR, ".first_block .second").send_keys("Petrov")
    browser.find_element(By.CSS_SELECTOR, ".first_block .third").send_keys("test@mail.com")

    # Отправляем форму
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # Проверяем результат
    welcome_text = browser.find_element(By.TAG_NAME, "h1").text
    assert "Congratulations! You have successfully registered!" == welcome_text


def test_registration2(browser):
    browser.get("http://suninjuly.github.io/registration2.html")

    # Новый вариант: проверяем количество обязательных полей
    required_fields = browser.find_elements(By.CSS_SELECTOR, "input[required]")
    assert len(required_fields) == 3, f"Expected 3 required fields, got {len(required_fields)}"

    # Заполняем все обязательные поля
    for field in required_fields:
        field.send_keys("Test")

    # Отправляем форму
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # Проверяем результат
    welcome_text = browser.find_element(By.TAG_NAME, "h1").text
    assert "Congratulations! You have successfully registered!" == welcome_text