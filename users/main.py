import csv

class Account:
    
    def __init__(self, acount_type, balance = 0 ):
        self.acount_type = acount_type
        self.balance = float(balance)
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError('Withdrawal amount must be greater than 0')
        if amount > self.balance:
            raise ValueError('Insufficient funds')
        self.balance -= amount
        return self.balance
        
        
    def deposit(self, amount):
        if 0 < amount :
            self.balance += amount
            return self.balance
        else:
            raise ValueError ('the amount must be greater than 0')





class Customer:
    def __init__(self, customer_id, Fname, Lname, password):
        self.customer_id = customer_id
        self.Fname = Fname
        self.Lname =Lname
        self.password = password
        self.accounts = {
            
        }
        
    def checking_account(self, balance = 0):
        if 'checking'not in self.accounts :
            self.accounts['checking'] = Account('checking', balance)
            return f'Checking account created ,  Your balance = {balance}'
        else:
            raise ValueError(f'You already have a checking account, your balance = {self.accounts['checking'].balance}')








            
if __name__ == '__main__':       
    test_account = Account("checking" , 1000)
    test_cheking_account = Customer(100, "Hassan", "Ali", "ASD@123")
    try:
        new_balance = test_account.deposit(1500)
        print(f"Deposit successful. New balance: {new_balance}")
    except ValueError as err:
        print(err)
        
    try:
        new_balance = test_account.withdraw(100)
        print(f"withdrawal successful. New balance: {new_balance}")
    except ValueError as err:
        print(err)
    
    try:
        check = test_cheking_account.checking_account(1000)
        print(check)
    except ValueError as err:
        print(err)

    # checking_account_again
    try:
        check = test_cheking_account.checking_account(2000)
        print(check)
    except ValueError as err:
        print(err)

        
