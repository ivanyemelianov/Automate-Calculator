from behave import given, when, then


@then('Divide function can divide every digit correctly')
def verify_can_divide_digits(context):
    context.app.main_page.verify_can_divide_digits()