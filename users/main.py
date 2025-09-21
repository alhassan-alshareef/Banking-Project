import csv

class acount:
    
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


if __name__ == '__main__':       
    test_account = acount("checking" , 1000)
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