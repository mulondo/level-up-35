import unittest
from signup import Signup


class Test(unittest.TestCase):
     def setUp(self):
         self.sign_up=Signup()

     def test_add_user(self):
         self.assertEqual(self.sign_up.add_user("moses", "12345"), {'moses':'12345'})


     def test_get_user(self):
         self.sign_up.add_user("moses", "12345")
         self.assertTrue(self.sign_up.get_user("moses"), msg="The user name is registered")

