import csv
import os 

class Account:
    
    def __init__(self, account_id, balance = 0 ):
        self.account_id = account_id
        self.balance = balance
        self.active = True
    
    def withdraw(self, amount):
        if not self.active:
            raise ValueError('Account is deactivated')
        if amount <= 0:
            raise ValueError('Withdrawal amount must be greater than 0')
        self.balance -= amount
        return self.balance
    
        
        
    def deposit(self, amount):
        if 0 >= amount :
            raise ValueError ('the amount must be greater than 0')
        self.balance += amount
        return self.balance
    
class Checking_Account(Account):
    def __init__(self, account_id, balance=0):
        super().__init__(account_id, balance)

class Savings_Account(Account):
    def __init__(self, account_id, balance=0):
        super().__init__(account_id, balance)

class Customer:
    def __init__(self, customer_id, Fname, Lname, password, balance_checking=None, balance_savings=None):
        self.customer_id = customer_id
        self.Fname = Fname
        self.Lname =Lname
        self.password = password
        
        if balance_checking is not None:
            self.checking_account = Checking_Account(customer_id,balance_checking)
        else:
            self.checking_account = None
            
        if balance_savings is not None:
            self.savings_account = Savings_Account(customer_id,balance_savings)
        else:
            self.savings_account = None
    
    def has_checking(self):
        return self.checking_account is not None

    def has_savings(self):
        return self.savings_account is not None
    
    def create_checking(self, ibalance=0):
        if self.has_checking():
            raise ValueError("Customer already has a checking account")
        self.checking_account = Checking_Account(self.customer_id, ibalance)
        return self.checking_account

    def create_savings(self, ibalance=0):
        if self.has_savings():
            raise ValueError("Customer already has a savings account")
        self.savings_account = Savings_Account(self.customer_id, ibalance)
        return self.savings_account
        




class Bank:
    
    def __init__(self, filename= "banck.csv"):
        
        self.filename = filename
        self.customers = {}
        self.loadCustomers()
        
    def loadCustomers(self):
        if not os.path.exists(self.filename):
            with open (self.filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['customer_id', 'Fname', 'Lname', 'password', 'balance_checking', 'balance_savings',])
        try:
            with open (self.filename, 'r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    customer_id = row['customer_id']
                    balance_checking = float(row['balance_checking']) if row['balance_checking'] else None
                    balance_savings = float(row['balance_savings']) if row['balance_savings'] else None
                    
                    customer = Customer(customer_id, row['Fname'], row['Lname'], row['password'],balance_checking,balance_savings)
                    self.customers[customer_id] = customer
        except Exception:
            print("Error loading customers:")
            
        
    def save_customers(self):
        try:
            with open (self.filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['customer_id', 'Fname', 'Lname', 'password', 'balance_checking', 'checking_active', 'balance_savings', 'savings_active'])
                for customer in self.customers.values():
                    balance_checking = customer.checking_account.balance if customer.has_checking() else ""
                    checking_active = str(customer.checking_account.active).lower() if customer.has_checking() else ""
                    
                    
                    balance_savings = customer.savings_account.balance if customer.has_savings() else ""
                    savings_active = str(customer.savings_account.active).lower() if customer.has_savings() else ""
        
                    writer.writerow([
                    customer.customer_id,
                    customer.Fname,
                    customer.Lname,
                    customer.password,
                    balance_checking,
                    checking_active,
                    balance_savings,
                    savings_active
                    ])
                    
                    
        except Exception:
            print("Error save customers:")
    
    def new_account_id(self):
        if self.customers:  
            customer_id = max(map(int,self.customers.keys())) + 1 
            while customer_id in self.customers:  
                customer_id += 1
        else:
            customer_id = 100
            
        return str(customer_id)

        





# try if save_customers work 
if __name__ == "__main__":
    bank = Bank("banck.csv")

    customer1 = Customer(
        customer_id="1001",
        Fname="Ali",
        Lname="alshareef",
        password="aa@1234",
        balance_checking=500,
        balance_savings=0
    )
    bank.customers[customer1.customer_id] = customer1
    bank.save_customers()
    
