from behave import *

@when('forgot_pswd: I set my email "{email}"')
def step_impl(context,email):
    context.forgot_pswd_page.set_email(email)

@then('forgot_pswd: I verify that email validation is correct')
def step_impl(context):
    context.forgot_pswd_page.verify_email_error_msg()


