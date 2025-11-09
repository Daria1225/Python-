from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def wait_until_images_loaded(driver):
    images = driver.find_elements(By.TAG_NAME, "img")
    for img in images:
        WebDriverWait(driver, 10).until(
            lambda d: d.execute_script("return arguments[0].complete && typeof arguments[0].naturalWidth != \"undefined\" && arguments[0].naturalWidth > 0", img))

if __name__ == "__main__":
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
        
        WebDriverWait(driver, 10).until(lambda d: len(d.find_elements(By.TAG_NAME, "img")) >= 3)
        
        wait_until_images_loaded(driver)
        
        third_image = driver.find_elements(By.TAG_NAME, "img")[2]
        
        print(third_image.get_attribute("src"))
    
    finally:
        driver.quit()