from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    # Функция для открытия url
    def open(self):
        self.driver.get(self.url)

    # метод для видимого элемента
    def element_is_visible(self, locator, timeout=5):
        # возвращаем ожидание драйвера в течение timeout до момента, когда
        # выполнятся условия visibility_of_element_located локатора элемента
        return wait(self.driver, timeout)\
            .until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=5):
        return wait(self.driver, timeout)\
            .until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=5):
        return wait(self.driver, timeout)\
            .until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator, timeout=5):
        return wait(self.driver, timeout)\
            .until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=5):
        return wait(self.driver, timeout)\
            .until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=5):
        return wait(self.driver, timeout)\
            .until(EC.element_to_be_clickable(locator))

    def goto_element(self, element):
        self.driver.execute_script("Argument[0].scrollIntoView();", element)

