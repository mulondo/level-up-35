import unittest
from signup import Signup


class Test(unittest.TestCase):
    def setUp(self):
        self.sign_up=Signup()

    def test_signup(self):
        self.assertIsInstance(self.sign_up, Signup,msg="Sign_up is not an install of class Signup")

    def test_add_user(self):
        self.assertEqual(self.sign_up.add_user("moses", "12345","mulondo26@gmail.com"), 
         [{'email':'mulondo26@gmail.com','username':'moses','password':'12345'}])


    def test_get_user(self):
        self.sign_up.add_user("mulondo", "12345678","mulo@gmail.com")
        self.assertTrue(self.sign_up.get_user("moses","mulo@gmail.com"), msg="The user name is not registered")

    def test_validation_input(self):
        self.assertRaises(TypeError,self.sign_up.validate_input, 1545,323)


    def test_check_length(self):
        self.assertEqual(self.sign_up.check_length(), 0)
        self.sign_up.add_user("peter", "958943","peter@gmail.com")
        self.assertEqual(self.sign_up.check_length(), 1)

    def test_change_password(self):
        self.sign_up.add_user("John1", "123456","jofhn@gmail.com")
        self.sign_up.add_user("John2", "123456","joghn@gmail.com")
        self.sign_up.add_user("John", "123456","johhn@gmail.com")
        self.assertTrue(self.sign_up.change_password("John","90433e"), msg="password not changed")
    
    def test_forgot_username(self):
       self.sign_up.add_user("paul", "123456","paul@gmail.com")
       self.assertTrue(self.sign_up.forgot_username("paul@gmail.com","123456"),msg="wrong email or password")
    
    def test_remove_user(self):
        self.sign_up.add_user("paul", "123456","paul@gmail.com")
        self.assertTrue(self.sign_up.remove_user("paul"),msg="The user was not found")
    
