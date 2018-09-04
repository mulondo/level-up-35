import unittest
from .signup import Signup


class Test(unittest.TestCase):
     def setUp(self):
         self.sign_up=Signup()

     def test_signup(self):
         self.assertIsInstance(self.sign_up, Signup,msg="Sign_up is not an install of class Signup")

     def test_add_user(self):
         self.assertEqual(self.sign_up.add_user("moses", "12345"), {'moses':'12345'})


     def test_get_user(self):
         self.sign_up.add_user("moses", "12345")
         self.assertTrue(self.sign_up.get_user("moses"), msg="The user name is not registered")

     def test_validation_input(self):
         self.assertTrue(self.sign_up.validate_input(254, 9932), msg="wrong input format")
         self.assertTrue(self.sign_up.validate_input("", ""), msg="Username and password is not empty")

     def test_check_length(self):
         self.assertEqual(self.sign_up.check_length(), 0)

     def test_change_password(self):
         self.sign_up.add_user("mulondo", "123456")
         self.assertTrue(self.sign_up.change_password("mulondo","90433e"), msg="password not changed")
