import time
from pages.elements_page import TextBoxPage
import pytest

@pytest.mark.usefixtures("driver")
class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page =TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page\
                .fill_all_fields()
            # сохраняем переменные output из тюпла функции check_filled_form()
            output_full_name, output_email, output_cur_addr, \
            output_per_addr = text_box_page.check_filled_form()
            # assert ключевое слово для проверки
            assert full_name == output_full_name, "full_name does not match"
            assert email == output_email, "email does not match"
            assert current_address == output_cur_addr\
                    , "current_address does not match"
            assert permanent_address == output_per_addr\
                , "permanent_address does not match"

            # код выше можно заменить более коротким
            # input_data = text_box_page.fill_all_fields()
            # output_data = text_box_page.check_filled_form()
            # assert input_data == output_data


