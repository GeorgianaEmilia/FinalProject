@regressionTest
Feature: Herokuapp login page tests

  Background:
    Given login: I am a user on Herokuapp in page

    # Test7 Completeaza cu user si pass invalide Click login Verifica ca mesajul de pe eroare e corect
  @herokuapp
  Scenario: Error message login page
    Given login: I set my email "bubu"
    When login: I set my pass "password"
    When login: I click login button
    Then login: I will see the error message "Your username is invalid!"

      # Test1 Verificam ca noul url e corect
  @herokuapp0
  Scenario: Check the new url
    Then login: I check if the new url is correct

          # Test4 Verificam ca butonul de login este displayed
  @herokuapp1
  Scenario: Login element is displayed
    Then login: I will see the login element is displayed

          # Test2 Verificam ca  page title e corect
  @herokuapp2
  Scenario: Page title is correct
    Then login: I will see if the title page is correct

       # Test3 Verificam textul de pe elementul xpath=//h2 e corect
  @herokuapp3
  Scenario: The text on the element is correct
    Then login: I will see if the element on the text is correct

      # Test5 Verificam ca atributul href al linkului ‘Elemental Selenium’ e corect
  @herokuapp4
  Scenario: The href attribute link for Elemental Selenium is correct
    Then login: I check that the href attribute of the link Elemental Selenium is correct

      # Test6 Lasam goale user si pass Click login Verificam ca eroarea e displayed login: I check if the error message is displayed
  @herokuapp5
  Scenario: The error message is displayed
    Then login: I check if the error message is displayed

    # Test8 Lasam goale user si pass Click login Apasam x la eroare Verificam ca eroarea a disparut
  @herokuapp6
  Scenario: The error message is not displayed
    When login: I click login button
    Then login: I check if the error message is not displayed

    # Test9 Ia ca o lista toate //label VerificaM textul ca textul de pe ele sa fie cel asteptat (Username si Password) Aici e ok sa avem 2 asserturi
  @herokuapp7
  Scenario: The labels message are correct
    Then login: I check if the message on the labels contain the correct message(username and password)


    # Test10 Verifica ca elementul cu clasa=’flash succes’ este displayed! Verifica ca mesajul de pe acest element CONTINE textul ‘secure area!’

  @herokuapp8
  Scenario: Validate the correct username and password
    Given login: I set my email "tomsmith"
    When login: I set my pass "SuperSecretPassword!"
    When login: I click login button
    Then login: I check if the attribute flash success is displayed and the message on the attribute contain the text "secure area"

    # Test11 Completeaza cu user si pass valide,Click login,Click logout,Verifica ca ai ajuns pe https://the-internet.herokuapp.com/login
  @herokuapp9
  Scenario: After logout I check the current URL
    Given login: I set my email "tomsmith"
    When login: I set my pass "SuperSecretPassword!"
    When login: I click login button
    When login: I click logout button
    Then login: I will check after logout if the current URL is "https://the-internet.herokuapp.com/login"

    # Test12 - brute force password hacking Completeaza user tomsmith,Gaseste elementul // h4 si ia  tot textul de pe el,Ia textul de pe el si fa split dupa spatiu.
    # Considera fiecare cuvant  ca o potentiala parola,Foloseste  o  structura iterativa prin care sa introduci rand pe rand parolele  si sa apesi pe login
    # La final  testul  trebuie  sa imi printeze ,‘Nu   am  reusit  sa gasesc parola’,‘Parola secreta este[parola]’

  @herokuapp10
  Scenario: Brute Force password hacking
    Then login: I check the entire combination of passwords