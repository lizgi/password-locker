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

