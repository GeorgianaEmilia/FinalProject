from pages.login_page import Login_page
from pages.forgot_pswd_page import Forgot_password_page
from pages.home_page import Home_page
from pages.sign_in_page import Sign_in_page
from browser import Browser

def before_all(context):
    context.browser = Browser()
    context.login_page = Login_page()
    context.forgot_pswd_page = Forgot_password_page()
    context.home_page= Home_page()
    context.sign_in_page=Sign_in_page()

def after_all(context):
    context.browser.close()

    #contextul este o cutiuta care contine cate un obiectde tipul fiecarei clase de pagini
    #before all=BDD
    #after all=BDD
    #de fiecare data cand adaugam o pagina noua in proiect o vom adauga in context