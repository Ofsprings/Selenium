import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestRegistration(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_registration1(self):
        self.browser.get("http://suninjuly.github.io/registration1.html")

        # Заполнение обязательных полей
        self.browser.find_element(By.CSS_SELECTOR, ".first_block .first").send_keys("Ivan")
        self.browser.find_element(By.CSS_SELECTOR, ".first_block .second").send_keys("Petrov")
        self.browser.find_element(By.CSS_SELECTOR, ".first_block .third").send_keys("test@mail.com")

        # Отправка формы
        self.browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        # Проверка успешной регистрации
        welcome_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_registration2(self):
        self.browser.get("http://suninjuly.github.io/registration2.html")

        # Попытка заполнить форму (вызовет NoSuchElementException)
        self.browser.find_element(By.CSS_SELECTOR, ".first_block .first").send_keys("Ivan")
        self.browser.find_element(By.CSS_SELECTOR, ".first_block .second").send_keys("Petrov")
        self.browser.find_element(By.CSS_SELECTOR, ".first_block .third").send_keys("test@mail.com")


if __name__ == "__main__":
    unittest.main()