from behave import given, when, then

@then('Subtract function can subtract every digit correctly')
def verify_can_add_two_digits(context):
    context.app.main_page.verify_can_subtract_two_digits()