class User:

    user_list = []

    def __init__(self, username, password):
        """
        method for user property
        """
        self.username = username
        self.password = password

    def save_user(self):
        """
         method to save user
        """
        User.user_list.append(self)
    
    @classmethod
    def display_user(cls):
        return cls.user_list

    def delete_user(self):
        '''
        delete_account(saved) method 
        '''
        User.user_list.remove(self)

class Credentials():

    credentials_list = []
    @classmethod
    def verify_user(cls,username, password):
        """
        method to verify whether the user is in our user_list or not
        """
        a_user = ""
        for user in User.user_list:
            if(user.username == username and user.password == password):
                    a_user == user.username
        return a_user

    def __init__(self,account,userName, password):
        """
        method that defines user credentials to be stored
        """        
        self.account = account
        self.userName = userName
        self.password = password
    
    def save_details(self):
        """
        method to store a new credential to the credentials list
        """
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        """
        delete_credentials method that deletes an account credentials from the credentials_list
        """
        Credentials.credentials_list.remove(self)


    
