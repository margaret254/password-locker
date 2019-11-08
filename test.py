import unittest 
from main import User
from main import Credentials

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Margaret","Maggie@254")
        # create user object

    def test_init(self):
        '''
        test_init to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.user_name,"Margaret")
        self.assertEqual(self.new_user.password,"Maggie@254")

if __name__=='__main__':
    unittest.main()

