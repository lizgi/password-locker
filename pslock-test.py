import unittest
from pslock import User
from pslock import Credentials

class TestClass(unittest.TestCase):
    """
    A Test class that defines test cases for the User class.
    """
    def setUp(self):
        
        self.new_user = User('ElizabethGikonyo','AbZ3thg3')

    def test_init(self):
        
        self.assertEqual(self.new_user.username,'ElizabethGikonyo')
        self.assertEqual(self.new_user.password,'AbZ3thg3')

    def test_save_user(self):
    
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)
