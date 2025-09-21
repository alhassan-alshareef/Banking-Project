import unittest

from users.main import acount

class testAcount(unittest.TestCase):
    
    def setUp(self):
        self.acc = acount('checking', 1000)
    
    def test_deposit_valid(self):
        
        self.acc.deposit(500)
        self.assertEqual(self.acc.balance, 1500)
    
    def test_withdraw_valid(self):
        self.acc.withdraw(300)
        self.assertEqual(self.acc.balance, 700)
    
    def test_withdraw_invalid(self):
        with self.assertRaises(ValueError):
            self.acc.withdraw(2000)
    
    def test_deposit_invalid(self):
        with self.assertRaises(ValueError):
            self.acc.deposit(0)