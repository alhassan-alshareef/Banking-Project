import unittest

from users.users import  Bank 

class TestBank(unittest.TestCase):
    def setUp(self):
        
        self.filename = 'banck.csv'
        self.bank = Bank(self.filename)
        
