#!/usr/bin/env python3.9
from pslock import User, Credentials

def create_new_user(username,password):
    '''
    Function to create a new user with a username and password
    '''
    new_user = User(username,password)
    return new_user

def save_user(user):
    '''
    Function to save a new user
    '''
    user.save_user()
def display_user():
    """
    Function to display existing user
    """
    return User.display_user()
def login_user(username,password):
    """
    function that checks user
    """
  
    check_user = Credentials.verify_user(username,password)
    return check_user

def create_new_credential(account,userName,password):
    """
    Function that creates new credentials for a given user account
    """
    new_credential = Credentials(account,userName,password)
    return new_credential
def save_credentials(credentials):
    """
    Function to save Credentials to the credentials list
    """
    credentials. save_details()
def display_accounts_details():
    """
    Function that returns all the saved credential.
    """
    return Credentials.display_credentials()

def delete_credential(credentials):
    """
    Function to delete a Credentials from credentials list

    """  
    credentials.delete_credentials()

def find_credential(account):
    """
    Function that finds a Credentials by an account name and returns the Credentials for it
    """
    return Credentials.find_credential(account)
def check_credendtials(account):
    """
    Function that check if a Credentials exists with that account name and return true or false

    """
    return Credentials.if_credential_exist(account)

def generate_Password():
    '''
    generates a random password for the user.
    '''
    auto_password=Credentials.generatePassword()
    return auto_password
def copy_password(account):
    """
    A funct that copies the password using the pyperclip framework
    We import the framework then declare a function that copies the emails.
    """
    return Credentials.copy_password(account)

def passlocker():
    print("Hello Welcome to your Accounts Password App..\n Please enter one of the following to proceed.\n CA ---  Create New Account  \n HA---  Have An Account  \n")
    short_code=input("").lower().strip()
    if short_code == "ca":
        print("Sign Up")
        print('*' * 50)
        username = input("User_name: ")
        while True:
            print(" IP - To input your own pasword:\n GP - To generate random Password")
            password_Choice = input().lower().strip()
            if password_Choice == 'ip':
                password = input("Enter Password\n")
                break
            elif password_Choice == 'gp':
                password = generate_Password()
                break
            else:
                print("Invalid password please try again")
                save_user(create_new_user(username,password))
        print("*"*85)
        print(f"Hello {username}, Your account has been created succesfully! Your password is: {password}")
        print("*"*17)
    elif short_code == "ha":
        print("*"*54)
        print("Enter your User name and your Password to log in:")
        print('*' * 50)
        username = input("User name: ")
        password = input("password: ")
        login = login_user(username,password)
        if login_user == login:
            print(f"Hello {username}.Welcome To PassWord Locker")  
            print('\n')
      