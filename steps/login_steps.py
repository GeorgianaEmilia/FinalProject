from behave import *

@given('login: I am a user on Herokuapp in page')
def step_impl(context):
    context.login_page.navigate_to_home_page()

@given('login: I set my email "{email}"')
def step_impl(context, email):
    context.login_page.set_email(email)

@when('login: I set my pass "{password}"')
def step_impl(context, password):
    context.login_page.set_pass(password)

@when('login: I click login button')
def step_impl(context):
    context.login_page.click_login_btn()

@when('login: I click logout button')
def step_impl(context):
    context.login_page.click_logout()

@then('login: I check if the new url is correct')
def step_impl(context):
    context.login_page.test_url()

@then('login: I will see the error message "{error_message}"')
def step_impl(context,error_message):
    context.login_page.validate_error_message(error_message)

@then('login: I will see the login element is displayed')
def step_impl(context):
    context.login_page.test_elem_displayed()

@then('login: I will see if the title page is correct')
def step_impl(context):
    context.login_page.test_page_title()

@then('login: I will see if the element on the text is correct')
def step_impl(context):
    context.login_page.test_login_pageh2_text()

@then('login: I check that the href attribute of the link Elemental Selenium is correct')
def step_impl(context):
    context.login_page.test_elem_atribute()

@then('login: I check if the error message is displayed')
def step_impl(context):
    context.login_page.test_error_displayed()

@then('login: I check if the error message is not displayed')
def step_impl(context):
    context.login_page.test_closeerror_correct()

@then('login: I check if the message on the labels contain the correct message(username and password)')
def step_impl(context):
    context.login_page.test_userandpass()

@then('login: I check if the attribute flash success is displayed and the message on the attribute contain the text "{header_message}"')
def step_impl(context,header_message):
    context.login_page.test_loginpage(header_message)

@then('login: I will check after logout if the current URL is "{current_url}"')
def step_impl(context,current_url):
    context.login_page.test_verificareURL(current_url)

@then('login: I check the entire combination of passwords')
def step_impl(context):
    context.login_page.test_pass_hacking()