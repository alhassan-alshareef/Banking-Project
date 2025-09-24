import unittest

from users.users import  Bank 

class TestBank(unittest.TestCase):
    def setUp(self):
        
        self.filename = 'banck.csv'
        self.bank = Bank(self.filename)
        
    def test_add_customer(self):
        customer = self.bank.add_new_customer( 'Hassan', 'Ali', 'awq@2341',  1000, 200)
        self.assertEqual(customer.Fname, 'Hassan') 
        self.assertEqual(customer.Lname, "Ali") 
        self.assertEqual(customer.checking_account.balance, 1000) 
        self.assertEqual(customer.savings_account.balance, 200)
        self.bank.save_customers()