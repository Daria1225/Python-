import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def setup_teardown():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_calculator(setup_teardown):
    driver = setup_teardown

    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    delay_input = driver.find_element(By.ID, "delay")
    delay_input.clear()
    delay_input.send_keys("45")

    button_7 = driver.find_element(By.XPATH, "//span[text()='7']")
    button_plus = driver.find_element(By.XPATH, "//span[text()='+']")
    button_8 = driver.find_element(By.XPATH, "//span[text()='8']")
    button_equal = driver.find_element(By.XPATH, "//span[text()='=']")

    button_7.click()
    button_plus.click()
    button_8.click()
    button_equal.click()
