# FinalProject
My name is Emilia, I’m 25 years old.
I graduated from the Faculty of Electronics, Communications and Computers in Pitesti.
I have been living in Bucharest for 3 years, where I worked as graphic designer at Makita and Expleo.
Curiosity for automated testing arose when a friend was hired as an automation tester and told me
how many challenges he has every day and the satisfaction of finding the solution, of solving a bug.
I started an automated testing course at IT Factory, the course was taught by Andy, the best teacher who supported and helped us all the time.

This repository contains one of the projects I worked on. From a technical point of view, the project is structured as follows:
- the programming language used is Python using the PYCHARM IDE
- BDD (BEHAVE DRIVEN DEVELOPMENT) methodology was used to write the tests
- as a design pattern I applied POM (PAGE OBJECT MODEL)
- test scenarios are in the 'features' package and the files have the extension '.feature'
- for the development of the project we used the following libraries:
  - selenium + webdriver (for accessing and manipulating the elements of the web page)
  - behave (for generating HTML report)

To use the project we have the following steps:
-installation of dependencies:
    - pip install -U selenium
    - pip install behave
    - pip install behave-html-formatter
    - pip install webdriver-manager
-we use command: behave -f html -o behave-report.html --tags = @ scenario
    - @ scenario = tag name for the test run

The final report is generated automatically after running the previously specified command and can be seen in the project root,
the file is called behave-report.html.
