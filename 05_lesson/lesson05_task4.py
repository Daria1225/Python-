from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from time import sleep


def test_login():
    try:
        # Создаем сервис для Firefox и инициализируем браузер
        service = FirefoxService() 
        driver = webdriver.Firefox(service=service)
        
        # Переходим на тестовую страницу
        driver.get("http://the-internet.herokuapp.com/login")
        
        # Ждем немного, чтобы убедиться, что страница загрузилась
        sleep(2)
        
        # Заполняем поля формы
        username_field = driver.find_element(By.ID, "username")
        password_field = driver.find_element(By.ID, "password")
        
        username_field.send_keys("tomsmith")
        password_field.send_keys("SuperSecretPassword!")
        
        # Нажимаем кнопку Login
        login_button = driver.find_element(By.CSS_SELECTOR, ".fa.fa-2x.fa-sign-in")
        login_button.click()
        
        # Ждем некоторое время, пока обработаются действия
        sleep(4)
        
        # Получаем и выводим текст с зелёной плашки
        success_message = driver.find_element(By.CLASS_NAME, "flash.success").text.strip()
        print(success_message)
    
    finally:
        # Закрываем браузер
        driver.quit()


if __name__ == "__main__":
    test_login()
    