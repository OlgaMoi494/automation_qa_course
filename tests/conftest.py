import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

@pytest.fixture(scope="function")
def driver():
    # данная команда запускает наш браузер
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    # команда открывает браузер по всей длине экрана
    driver.maximize_window()
    # 2 команды выше запускаются перед выполнением нашего теста
    # если нам нужно что то выполнить в тер-даун фикстуре, то прописываем yield
    yield driver
    driver.quit()

# def test(driver):
#     driver.get("https://www.google.com")
#     time.sleep(10)