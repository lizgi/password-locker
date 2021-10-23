import unittest
from pslock import User
from pslock import Credentials

class TestClass(unittest.TestCase):

    def setUp(self):
        
        self.new_user = User('ElizabethGikonyo','AbZ3thg3')

    def test_init(self):
        
        self.assertEqual(self.new_user.username,'ElizabethGikonyo')
        self.assertEqual(self.new_user.password,'AbZ3thg3')

    def test_save_user(self):
    
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

class TestCredentials(unittest.TestCase):
    
    def setUp(self):
        
        self.new_credential = Credentials('Gmail','gikonyo.elizabeth','op5Gij43')
    def test_init(self):
        
        self.assertEqual(self.new_credential.account,'Gmail')
        self.assertEqual(self.new_credential.userName,'gikonyo.elizabeth')
        self.assertEqual(self.new_credential.password,'op5Gij43')

    def save_credential_test(self):
        
        self.new_credential.save_details()
        self.assertEqual(len(Credentials.credentials_list),1)


    def test_save_many_accounts(self):

        self.new_credential.save_details()
        test_credential = Credentials("Twitter","lizgikonyo","Bq68pfk@") 
        test_credential.save_details()
        self.assertEqual(len(Credentials.credentials_list),2)

    def test_delete_credential(self):
      
        self.new_credential.save_details()
        test_credential = Credentials("Twitter","lizgikonyo","Bq68pfk@")
        test_credential.save_details()

        self.new_credential.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_find_credentialr(self):
       
        self.new_credential.save_details()
        test_credential = Credentials("Twitter","lizgikonyo","Bq68pfk@") 
        test_credential.save_details()

        the_credential = Credentials.find_credential("Twitter")

        self.assertEqual(the_credential.account,test_credential.account)
    
