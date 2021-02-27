from selenium.webdriver.common.by import By
from pages.base_page import Page


class MainPage(Page):
    MODE = (By.ID, 'com.google.android.calculator:id/mode')
    FORMULA_FIELD = (By.ID, 'com.google.android.calculator:id/formula')

    FINAL_RESULT = (By.ID, 'com.google.android.calculator:id/result_final')
    RESULT_PREVIEW = (By.ID, 'com.google.android.calculator:id/result_preview')
    CLEAR = (By.ID, 'com.google.android.calculator:id/clr')

    decimal_point = 'com.google.android.calculator:id/dec_point'
    EQUALS = (By.ID, 'com.google.android.calculator:id/eq')
    DELETE = (By.ID, 'com.google.android.calculator:id/del')
    DIVIDE_BTN = (By.ID,'com.google.android.calculator:id/op_div')
    MULTIPLY_BTN = (By.ID, 'com.google.android.calculator:id/op_mul')
    SUB_BTN = (By.ID, 'com.google.android.calculator:id/op_sub')
    ADD_BTN = (By.ID, 'com.google.android.calculator:id/op_add')

    ARROW = (By.ID, 'com.google.android.calculator:id/arrow')

    DIGIT_BTNS = [
        (By.ID, 'com.google.android.calculator:id/digit_0'),
        (By.ID, 'com.google.android.calculator:id/digit_1'),
        (By.ID, 'com.google.android.calculator:id/digit_2'),
        (By.ID, 'com.google.android.calculator:id/digit_3'),
        (By.ID, 'com.google.android.calculator:id/digit_4'),
        (By.ID, 'com.google.android.calculator:id/digit_5'),
        (By.ID, 'com.google.android.calculator:id/digit_6'),
        (By.ID, 'com.google.android.calculator:id/digit_7'),
        (By.ID, 'com.google.android.calculator:id/digit_8'),
        (By.ID, 'com.google.android.calculator:id/digit_9'),
    ]

    def verify_digit_text(self):
        for i in range(9):
            item_in_digits = self.find_element(*self.DIGIT_BTNS[i]).text
            assert int(item_in_digits) == i, f"Expected {i} in {item_in_digits}"
            i += 1

    def verify_mode_text_deg(self):
        mode_text = self.find_element(*self.MODE).text
        assert 'DEG' in mode_text, f"Expected 'DEG' in {mode_text}"

    def verify_mode_text_rad(self):
        mode_text = self.find_element(*self.MODE)
        mode_text.click()
        assert 'RAD' in mode_text.text, f"Expected 'RAD' in {mode_text}"

    def verify_can_add_two_digits(self):
        self.wait(5)
        equals_btn = self.find_element(*self.EQUALS)
        add_btn = self.find_element(*self.ADD_BTN)

        for x in range(9):
            x = self.find_element(*self.DIGIT_BTNS[x])
            for y in range(9):
                y = self.find_element(*self.DIGIT_BTNS[y])
                self.wait(10)
                x.click()
                self.wait(5)
                add_btn.click()
                self.wait(5)
                y.click()
                self.wait(5)
                equals_btn.click()
                self.wait(5)
                final_result = int(self.find_element(*self.FINAL_RESULT).text)
                expected_result = int(x.text) + int(y.text)
                print(expected_result, final_result)
                assert expected_result == final_result, f'{x.text} + {y.text} should be equal to {expected_result}'

    def verify_can_subtract_two_digits(self):
        self.wait(20)
        equals_btn = self.find_element(*self.EQUALS)
        subtract_btn = self.find_element(*self.SUB_BTN)
        # delete = self.find_element(*self.DELETE)

        for x in range(9):
            self.wait(10)
            x = self.find_element(*self.DIGIT_BTNS[x])
            for y in range(9):
                self.wait(10)
                y = self.find_element(*self.DIGIT_BTNS[y])
                self.wait(20)
                # might need an extra click to remove the advanced functions drawer
                # x.click()
                # delete.click()
                x.click()
                self.wait(5)
                subtract_btn.click()
                self.wait(5)
                y.click()
                self.wait(5)
                equals_btn.click()
                self.wait(5)
                final_result = self.find_element(*self.FINAL_RESULT).text
                # print(final_result, type(final_result))
                # for some reason int() was not converting '-X' strings to ints
                if not final_result.isdigit():
                    final_result = int(final_result[1:]) * (-1)
                else:
                    final_result = int(final_result)
                expected_result = int(x.text) - int(y.text)
                print(expected_result, type(expected_result), final_result, type(final_result))
                assert expected_result == final_result, f'{x.text} - {y.text} should be equal to {expected_result}'

    def verify_can_multiply_digits(self):
        self.wait(10)
        equals_btn = self.find_element(*self.EQUALS)
        multiply_btn = self.find_element(*self.MULTIPLY_BTN)

        for x in range(9):
            x = self.find_element(*self.DIGIT_BTNS[x])
            for y in range(9):
                y = self.find_element(*self.DIGIT_BTNS[y])
                self.wait(10)
                x.click()
                self.wait(5)
                multiply_btn.click()
                self.wait(5)
                y.click()
                self.wait(5)
                equals_btn.click()
                self.wait(5)
                final_result = int(self.find_element(*self.FINAL_RESULT).text)
                expected_result = int(x.text) * int(y.text)
                # print(expected_result, final_result)
                assert expected_result == final_result, f'{x.text} * {y.text} should be equal to {expected_result}'

    def verify_can_divide_digits(self):
        self.wait(10)
        equals_btn = self.find_element(*self.EQUALS)
        divide_btn = self.find_element(*self.DIVIDE_BTN)
        delete = self.find_element(*self.DELETE)

        for x in range(9):
            x = self.find_element(*self.DIGIT_BTNS[x])
            for y in range(9):
                y = self.find_element(*self.DIGIT_BTNS[y])
                self.wait(10)
                x.click()
                self.wait(5)
                divide_btn.click()
                self.wait(5)
                y.click()
                self.wait(5)
                equals_btn.click()
                self.wait(5)
                if y.text != '0':
                    final_result = round(float(self.find_element(*self.FINAL_RESULT).text), 2)
                    expected_result = int(x.text) / int(y.text)
                    # print(expected_result, final_result)
                    assert round(expected_result, 2) == final_result, f'{x.text} / {y.text} should be equal to {expected_result}'
                else:
                    final_result = self.find_element(*self.RESULT_PREVIEW).text
                    expected_result = "Can't divide by 0"
                    delete.click()
                    delete.click()
                    delete.click()
                    assert expected_result == final_result, f'User should see a warning: {expected_result}'

