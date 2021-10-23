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
