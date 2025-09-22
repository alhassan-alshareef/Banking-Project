import unittest

from users.users import Account

from users.users import Customer

class testAcount(unittest.TestCase):
    
    def setUp(self):
        self.acc = Account('checking', 1000)
    
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
            
            
class testCustomer(unittest.TestCase):
    

    def setUp(self):
        self.customer = Customer(100, "Hassan", "Ali", "ASD@123")

    def test_checking_account(self):
        self.customer.checking_account(600)
        self.assertEqual(self.customer.accounts['checking'].balance, 600)

    def test_checking_account_again(self):
        self.customer.checking_account(600)
        with self.assertRaises(ValueError):
            self.customer.checking_account(1000)
        self.assertEqual(self.customer.accounts['checking'].balance,600)
        
        
    def test_saving_account(self):
        self.customer.saving_account(60)
        self.assertEqual(self.customer.accounts['saving'].balance, 60)

    def test_saving_account_again(self):
        self.customer.saving_account(30)
        with self.assertRaises(ValueError):
            self.customer.saving_account(100)
        self.assertEqual(self.customer.accounts['saving'].balance,30)