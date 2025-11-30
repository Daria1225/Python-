import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class TestShop:

    def setup_method(self):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 30)

    def teardown_method(self):
        self.driver.quit()

    def test_shop_purchase(self):
        """
        Тест: покупка товаров в интернет‑магазине saucedemo.
        Шаги:
        1. Открыть сайт.
        2. Авторизоваться как standard_user.
        3. Добавить в корзину 3 товара.
        4. Перейти в корзину и начать оформление заказа.
        5. Заполнить форму доставки.
        6. Проверить итоговую сумму ($58.29).
        """
        self.driver.get('https://www.saucedemo.com/')

        username_input = self.wait.until(
            EC.element_to_be_clickable((By.ID, 'user-name'))
        )
        username_input.send_keys('standard_user')

        password_input = self.wait.until(
            EC.element_to_be_clickable((By.ID, 'password'))
        )
        password_input.send_keys('secret_sauce')

        login_button = self.wait.until(
            EC.element_to_be_clickable((By.ID, 'login-button'))
        )
        login_button.click()

        backpack_add_btn = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[@class='inventory_item' and .//div[text()='Sauce Labs Backpack']]//button[text()='Add to cart']")
            )
        )
        backpack_add_btn.click()

        tshirt_add_btn = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[@class='inventory_item' and .//div[text()='Sauce Labs Bolt T-Shirt']]//button[text()='Add to cart']")
            )
        )
        tshirt_add_btn.click()

        onesie_add_btn = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[@class='inventory_item' and .//div[text()='Sauce Labs Onesie']]//button[text()='Add to cart']")
            )
        )
        onesie_add_btn.click()

        cart_link = self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'shopping_cart_link'))
        )
        cart_link.click()

        checkout_btn = self.wait.until(
            EC.element_to_be_clickable((By.ID, 'checkout'))
        )
        checkout_btn.click()

        first_name_input = self.wait.until(
            EC.element_to_be_clickable((By.ID, 'first-name'))
        )
        first_name_input.send_keys('Дарья')

        last_name_input = self.wait.until(
            EC.element_to_be_clickable((By.ID, 'last-name'))
        )
        last_name_input.send_keys('Меркулова')

        zip_code_input = self.wait.until(
            EC.element_to_be_clickable((By.ID, 'postal-code'))
        )
        zip_code_input.send_keys('123456')

        continue_btn = self.wait.until(
            EC.element_to_be_clickable((By.ID, 'continue'))
        )
        continue_btn.click()

        total_element = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'summary_total_label'))
        )
        total_text = total_element.text.strip().split(': ')

        actual_total = float(total_text[-1][1:])
        expected_total = 58.29
        
        assert actual_total == expected_total, \
            f'Ожидаемая сумма: ${expected_total}, фактическая: ${actual_total}'
