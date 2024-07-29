import time

from generator.generator import generated_person
from locators.elements_page_locators import TextBoxPageLocators
from pages.base_page import  BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    # мызаполнем данные, где их взять
    def fill_all_fields(self):
        # берем из генератора по одному значению Person
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        # элемент должен быть видимым
        # метод send_keys() симулируем typing в элемент
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS)\
                                    .send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS)\
                                    .send_keys(permanent_address)
        # теперь нам нужно все это отправить, нажать кнопку submit
        #self.element_is_visible(self.locators.SUBMIT).click()
        # Скроллинг до элемента перед кликом
        submit_button = self.element_is_visible(self.locators.SUBMIT)
        self.driver.execute_script("arguments[0].scrollIntoView();", submit_button)
        submit_button.click()
        return full_name, email, current_address, permanent_address
    # проверяем введенную информацию
    def check_filled_form(self):
        # выводим текстовые значения введенных полей
        # избавляемся от названий полей до знака : Name:, Email:...
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME)\
            .text.split(":")[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL)\
            .text.split(":")[1]
        current_address = self.element_is_present(self.locators
                                .CREATED_CURRENT_ADDRESS).text.split(":")[1]
        permanent_address = self.element_is_present(self.locators
                                .CREATED_PERMANENT_ADDRESS).text.split(":")[1]
        return full_name, email, current_address, permanent_address
