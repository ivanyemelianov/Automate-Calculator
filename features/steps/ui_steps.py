from behave import given, when, then

@given('Application is running')
def app_is_running(context):
    pass

@when('Main page is open')
def main_page_open(context):
    pass

@then('Text of the button is set correctly')
def verify_digit(context):
    context.app.main_page.verify_digit_text()

@then('Text of DEG mode is set correctly')
def verify_deg_mode_text(context):
    context.app.main_page.verify_mode_text_deg()

@when('Change mode')
def change_mode(context):
    pass

@then('Text of RAD mode is set correctly')
def verify_rad_mode_text(context):
    context.app.main_page.verify_mode_text_rad()
