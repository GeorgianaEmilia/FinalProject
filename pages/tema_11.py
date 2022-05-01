''' 1.Avand ca exemplu pagina https://the-internet.herokuapp.com/login

Feature: User Authentication

Mergeti backwards si ganditi ca un product owner

Generati un epic (doar o propozitie care sa descrie functionalitatea majora ce urmeaza sa fie dezvoltata)

#Development of an authentication page that will contain user credentials and password.

2.Generati un user story pentru login care sa aiba 2 acceptance criteria

USER STORY: As a user, I want to insert user and password so that the system will check this credentials in the database.
Un login valid (positive) -> 

ACCEPTANCE CRITERIA: 
GIVEN that I insert the correct user and password,WHEN I go to click the login button, THEN I`m successfully redirect to secure page.

Un login Invalid (negative) ->

ACCEPTANCE CRITERIA: 
GIVEN that I insert the incorrect user and password, WHEN I go to click the login button, THEN appear the error message " Your password is invalid!"

3.
Generati un alt user story care acopere functionalitatea de register. Sa contina 2 acceptance criteria
Email e nou, deci user poate face register (positive)
Email e deja existent in baza de date (negative)

USER STORY:
As a new user, I want to register by creating a username and password so that the system can remember me and my data.

ACCEPTANCE CRITERIA: Email e nou, deci user poate face register (positive)

GIVEN that I am a registered user on heroku login page, WHEN I enter correct username and email, THEN I can access the application and my data.

ACCEPTANCE CRITERIA:Email e deja existent in baza de date (negative)
GIVEN that I insert a  existing email and password, WHEN I go to click the register button, THEN the system will check email in database
AND if it s present I will see a pop up with recover the password AND an error message "The email exist in our system"

4.Generati un ultim user story care sa acopere functionalitatea de reset password. Sa contina 2 acceptance criteria
Email e in baza de date
Email nu e in baza de date

USER STORY:
As a user, I want to reset my password so that the system will check if my email it s in database or not.

ACCEPTANCE CRITERIA:Email e in baza de date
GIVEN that I insert the correct email, WHEN I click the reset password button, THEN the system will check if email it s in database AND send
an email with reset password link.

ACCEPTANCE CRITERIA:Email nu e in baza de date
GIVEN that I insert the incorrect email, WHEN I click the reset password button, THEN the system will check if email it s in database
AND if not, appear an error message "The email are not registered"

5.
Impementati 3 pagini in noul proiect BDD cu POM
Home page https://the-internet.herokuapp.com/
Sa aiba cel putin 3 elemente inlcusiv Form Authentication
Sa contina metode de click pe ele
Login page https://the-internet.herokuapp.com/login
Sa contina user, pass, login_btn si metode pt interactiune cu ele
Secure page https://the-internet.herokuapp.com/secure
Sa contina mesajul de succes si verificare ca e displayed
Sa contina logout_btn si click pe el
'''