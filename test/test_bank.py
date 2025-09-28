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
        
    def test_deposit_into_checking(self):
        customer = self.bank.add_new_customer('waleed','Khaled','Wa@dd3256472',3000,None)
        customer.checking_account.deposit(2000)
        self.assertEqual(customer.checking_account.balance,5000)
        with self.assertRaises(ValueError): 
            customer.checking_account.deposit(-90)
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
        
    def test_deposit_into_savings(self):
        customer = self.bank.add_new_customer('jana','QQ',"JA@gfr2005",None,1000)
        customer.savings_account.deposit(1000)
        self.assertEqual(customer.savings_account.balance,2000)
        with self.assertRaises(ValueError): 
            customer.savings_account.deposit(-150)
        self.bank.save_customers()    
            


    def test_transfer_saving_to_checking(self):
        customer = self.bank.add_new_customer('John','Sam','pass@567',2000,1500)
        self.bank.transfer(
            sender_id=customer.customer_id,
            recipient_id=customer.customer_id,
            amount=500,
            from_account_type='savings',
            to_account_type='checking'
        )
        
        self.assertEqual(customer.checking_account.balance,2500) 
        self.assertEqual(customer.savings_account.balance, 1000) 
        self.bank.save_customers()

    def test_transfer_to_another_customer(self):
        customer1 = self.bank.add_new_customer('jasmine','tookes','jaz111&min',2000,4000)
        customer2 = self.bank.add_new_customer('selena','mitski','sel&2322ski',1600,3000)
        self.bank.transfer(
            sender_id=customer1.customer_id,
            recipient_id=customer2.customer_id,
            amount=500,
            from_account_type='checking',
            to_account_type='savings'
    )
        self.assertEqual(customer1.checking_account.balance,1500) 
        self.assertEqual(customer2.savings_account.balance, 3500) 
        self.bank.save_customers()


if __name__ == "__main__":
    unittest.main()