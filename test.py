import unittest 
from main import User

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Margaret","Mwangi","07123456789","Maggie@254","1234")
        # create user object

    def test_init(self):
        '''
        test_init to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.first_name,"Margaret")
        self.assertEqual(self.new_user.last_name,"Mwangi")
        self.assertEqual(self.new_user.phone_number,"0712345689")
        self.assertEqual(self.new_user.email,"Maggie@254")
        self.assertEqual(self.new_user.password,"1234")

if __name__=='__main__':
    unittest.main()

