# Selenium_Bot_Trelo

### Description
Example Selenium test project for trello.com. 
In project demonstration how Selenium app add card / delete card.  
Also app is creation auto reports. Project only for education.

### [Demostration video on youtube](https://youtu.be/cN2KOcJCkgw)


### Tools for testing
* PyTest
* Selenium
* PyTestHTML

### [Project Trello.com](https://trello.com/)

### You need
* [Python 3.9](https://www.python.org/downloads/release/python-390/)
* [Google Chrome Browser](https://www.google.com/intl/ru_ru/chrome/)
* [Selenium ChromeDriver.](https://chromedriver.chromium.org/) 

## WARNING!

### You account in [Attlassian](https://id.atlassian.com/), not in trello.com

### Environment
I used this test project on Mac OS. For Windows command must be changed, but parameters is same

## How deploy project

    git clone https://github.com/l-GreeN-l/Selenium_Bot_Trelo.git

    python3 -m venv venv

    source venv/bin/activate

    pip install -r requarements.txt

    mkdir reports
    
### Before launch

You need add names labels in your account in trello Name labels need to add in labels file.  
The name of each label must start on a new line.   
In root have file "labels.txt" - this is example. 

## Start project

### Marks
    card  - pytest mark for run all tests
    smoke - pytest mark for run only smoke tests



### Parameters for run
Parameter | Description
---- | ----
-m | pytest marks - "card"
--login | Your login/mail in account Atlassian
--password | Your password in account Atlassian
--url | https://trello.com/
--boardname | name of Kanban board
--groupname | name of group (Backlog, Test ...) Here add your card
--member | mail/login for send invite to card
--loacation | location on Google Maps
--labels | .txt filename with labels
--cardname | Example : "Task-001"
html | file name your report


### Example command for start:
i would recommend create shell file with start command.

    #!/bin/sh
    python3.9 -m pytest -m "card" --login=admin --password=123 --url=https://trello.com/ --boardname="Kanban Test" --groupname="Backlog" --member=admins_friend_login, --location="Russia Moscow" --labels=labels.txt --cardname="Task-001" -s -v --html=reports/trelo_test_$(date +%d-%m-%Y-%H).html --self-contained-html tests/
    
### Useful Links
What? | Links
---- | ----
Instalation guide Mac OS with Homebrew |  https://formulae.brew.sh/cask/chromedriver
Question | https://stackoverflow.com/questions/50086506/brew-install-chromedriver-not-working
