from behave import *

# given!, when!, and, but, then! - sintaxa gherkin
# given - seteaza situatia initiala
# when - pasii din test
# then - verificarea din test

@given('sign_in: I am a user on Jules sign in page')
def step_impl(context):
    context.sign_in_page.navigate_to_sign_in_page()

@when('sign_in: I set my email "{email}"')
def step_impl(context, email):
    context.sign_in_page.set_email(email)

@when('sign_in: I set my pass "{password}"')
def step_impl(context,pswd):
    context.sign_in_page.set_pass(pswd)

@when('sign_in: I click login button')
def step_impl(context):
    context.sign_in_page.click_login_btn()

@when('sign_in: I click forgot password link')
def step_impl(context):
    context.sign_in_page.click_forgot_pswd_link()



