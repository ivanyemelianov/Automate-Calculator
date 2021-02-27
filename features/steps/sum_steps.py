from behave import given, when, then

@then('Add function can add every digit correctly')
def verify_can_add_two_digits(context):
    context.app.main_page.verify_can_add_two_digits()