from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_fill_form():
    driver = webdriver.Edge()
    driver.maximize_window()

    driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
    driver.execute_script("document.body.style.zoom='75%'")
    wait = WebDriverWait(driver, 30)

    fields = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }

    for field_name, value in fields.items():
        field = wait.until(EC.element_to_be_clickable((By.NAME, field_name)))
        field.clear()
        field.send_keys(value)

    submit_button = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "button[type='submit']"))
    )
    submit_button.click()

    for locator in fields:
        assert "alert-success" in driver.find_element(By.ID, locator).get_attribute("class")

        assert "alert-danger" in driver.find_element(By.ID, "zip-code").get_attribute("class")

if __name__ == "__main__":
    test_fill_form()
