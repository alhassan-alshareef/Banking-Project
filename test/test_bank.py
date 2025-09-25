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
        
    def test_add_customer_savingsAccount(self):
        customer = self.bank.add_new_customer( 'ahmed', 'mohammed', 'awq@203421',  None, 200)
        self.assertEqual(customer.Fname, 'ahmed') 
        self.assertEqual(customer.Lname, "mohammed") 
        self.assertIsNone(customer.checking_account) 
        self.assertEqual(customer.savings_account.balance, 200)
        self.bank.save_customers()
        
    def test_add_customer_checkingAccount(self):
        customer = self.bank.add_new_customer( 'Alix', 'jhon', 'wqawq@23',  1000, None)
        self.assertEqual(customer.Fname, 'Alix') 
        self.assertEqual(customer.Lname, "jhon") 
        self.assertEqual(customer.checking_account.balance, 1000) 
        self.assertIsNone(customer.savings_account)
        self.bank.save_customers()
    
    def test_add_customer_with_weak_password(self):
        with self.assertRaises(ValueError) :
            self.bank.add_new_customer("mark", "Jhon", "weak123", 500, 0)
            
            
    def test_add_customer_with_strong_password(self):
        customer = self.bank.add_new_customer("Sara", "Smith", "Aa@12345", 1000, None)
        self.assertEqual(customer.Fname, "Sara")
        self.assertEqual(customer.Lname, "Smith")
        self.assertEqual(customer.checking_account.balance, 1000)
        self.assertIsNone(customer.savings_account)
        self.bank.save_customers()
        



if __name__ == "__main__":
    unittest.main()