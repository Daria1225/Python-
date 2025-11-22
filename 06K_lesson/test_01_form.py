from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_fill_form():
    driver = webdriver.Edge()
    driver.maximize_window()

    try:
        driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
        driver.execute_script("document.body.style.zoom='75%'")
        wait = WebDriverWait(driver, 30)

        fields = {
            "first-name": "Иван",
            "last-name": "Петров",
            "address": "Ленина, 55-3",
            "e-mail": "test@skypro.com",
            "phone": "+7985899998787",
            "zip-code": "",
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

        try:
            zip_field = wait.until(
                EC.presence_of_element_located((By.ID, "zip-code"))
            )
            zip_color = zip_field.value_of_css_property("border-color").lower()
            assert (zip_color == "rgb(245, 194, 199)"), f"ZIP не красный: {zip_color}"
        except:
            driver.save_screenshot("error_zip_code.png")
            raise

        green_fields = [name for name in fields.keys() if name != "zip-code"]
        for field_name in green_fields:
            field = wait.until(
                EC.presence_of_element_located((By.ID, field_name))
            )
            color = field.value_of_css_property("border-color").lower()
            assert (color == "rgb(186, 219, 204)"), f"{field_name} не зелёный: {color}"


        print("✅ Тест пройден!")


    except Exception as e:
        print(f"❌ Ошибка: {type(e).__name__}: {e}")
        driver.save_screenshot("error.png")
        raise
    finally:
        driver.quit()

if __name__ == "__main__":
    test_fill_form()
