from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    driver.get("http://uitestingplayground.com/textinput")
    
    input_field = driver.find_element(By.ID, "newButtonName")
    input_field.send_keys("SkyPro")
    
    button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
    button.click()
    
    updated_button_text = button.text.strip()
    
    if updated_button_text == "SkyPro":
        print(updated_button_text)
    else:
        print("Ошибка: Текст кнопки отличается от ожидаемого.")
finally:
    driver.quit()