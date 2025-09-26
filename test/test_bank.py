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
        
    def test_withdraw_checking(self): 
        customer = self.bank.add_new_customer('abc', 'ssa', 'pass@123word', 800, None) 
        customer.checking_account.withdraw(250) 
        self.assertEqual(customer.checking_account.balance, 550) 
        self.assertIsNone(customer.savings_account)
        with self.assertRaises(ValueError): 
            customer.checking_account.withdraw(800)
        with self.assertRaises(ValueError): 
            customer.checking_account.withdraw(-200) 
        self.bank.save_customers() 
        
    def test_withdraw_overdraftChecking(self):
        customer = self.bank.add_new_customer('leo','ass','pass@1234',200,100)
        customer.checking_account.withdraw(300)  
        self.assertEqual(customer.checking_account.balance,-135)  
        self.bank.save_customers()
    
    def test_savings_overdraft(self):
        customer = self.bank.add_new_customer('max','mac','pass@1234',100,300)
        customer.savings_account.withdraw(310)
        self.assertEqual(customer.savings_account.balance, -45)
        self.bank.save_customers()    

    def test_overdraft_deactivate(self):
        customer = self.bank.add_new_customer('basil','ahmed','pass@4321',100,300)
        new_balance = customer.checking_account.withdraw(120) 
        self.assertEqual(new_balance, -55) 
        self.assertEqual(customer.checking_account.overdraftCount, 1) 
        self.assertTrue(customer.checking_account.active) 
        new_balance = customer.checking_account.withdraw(10) 
        self.assertEqual(new_balance, -100) 
        self.assertEqual(customer.checking_account.overdraftCount, 2) 
        self.assertFalse(customer.checking_account.active)
        self.bank.save_customers()
        
    def test_withdraw_savings(self): 
        customer = self.bank.add_new_customer("Alix", 'XX', 'AAx552@322', None, 1100) 
        customer.savings_account.withdraw(500) 
        self.assertEqual(customer.savings_account.balance, 600) 
        with self.assertRaises(ValueError): 
            customer.savings_account.withdraw(1100) 
        with self.assertRaises(ValueError): 
            customer.savings_account.withdraw(-200)
        self.bank.save_customers()        
   
        


if __name__ == "__main__":
    unittest.main()