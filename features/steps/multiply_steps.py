from behave import given, when, then


@then('Multiply function can subtract every digit correctly')
def verify_can_multiply_digits(context):
    context.app.main_page.verify_can_multiply_digits()