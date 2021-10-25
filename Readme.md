# PASSWORD-LOCKER

## Author
***Elizabeth Gikonyo**

## Description
This is a python application that manages sign-in and Sign-up credentials of a person for various accounts. The credentials are usernames and Passwords for each account. It also stores the passwords and generates a unique password.

## Set-up instructions
### Install
Python3.9 for setup.

### Cloning my repository:
* Open Terminal {Ctrl+Alt+T}

* git clone git@https://github.com/lizgi/password-locker

* cd Password-locker

* code . / atom . 

## How to Run the application!
To run the application, open the cloned file in terminal and run the following commands:

      $ chmod +x app.py

      $ ./app.py

To run test for the application *use $ python3.9 pslock_test.py

## User Story
As a user I would like to... :

1. To create an account for the application or log into the application if already user has an account.

2. Store my existing acounts login details for various accounts that I have registered for.

3. Generate new password for an account that I haven't registered for and store it with the account name.

4. Delete stored account login details that are no longer useful.

5. Copy my credentials to the clipboard.

## BDD

| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
|Open the application on the terminal | Run the command ```$ ./app.py```|Hello Welcome to your Accounts Password Store... <br>* CA ---  Create New Account * HA ---  Have An Account |
|Select  CA| input username and password| Hello ```username```, Your account has been created succesfully! Your password is: ```password```|
|Select LI  | Enter your password and username you signed up with| Abbreviations menu to help you navigate through the application|
|Store a new credential in the application| Enter ```CC```|Enter Account, username, password<br>choose ```tp``` to enter your password or ```gp``` for the application to generate a password for you |
|Display all stored credentials | Enter ```DC```|A list of all credentials that has been stored or ```You don't have any credentials saved yet``` |
|Find a stored credential based on account name|Enter ```FC```| Enter the Account Name you want to search for and returns the account details|
|Delete an existing credential that you don't want anymore|Enter ```D```|Enter the account name of the Credentials you want to delete and returns true if the account has been deleted and false if the account doesn't exixt|
|Exit the application| Enter ```D```| The application exits|

## Technology Used
* Python3.9
* pip
* pyperclip

## Contact Informarion
If you have any question or contributions, please email me at[elizabeth.gikonyo@student.moringaschool.com]

## License


* Copyright (c) 2021 Lizzy

