import csv
import os 
import re

class Account:
    
    def __init__(self, account_id, balance = 0 ):
        self.account_id = account_id
        self.balance = balance
        self.overdraftCount = 0
        self.active = True
    
    def withdraw(self, amount):
        if not self.active:
            raise ValueError('Account is deactivated')
        if amount <= 0:
            raise ValueError('Withdrawal amount must be greater than 0')

        new_balance = self.balance - amount
        if  new_balance< -100:
            raise ValueError("account cannot have a resulting balance of less than -$100.")

        self.balance = new_balance 
        if self.balance < 0:
            self.balance -=35
            self.overdraftCount += 1
            print('Overdraft occurred — $35 fee added to your balance.')
            
            if self.overdraftCount >= 2:
                self.active = False
                print('Account has been deactivated ') 
        
        
        return self.balance
    
    def deposit(self, amount):
        if 0 >= amount :
            raise ValueError ('the amount must be greater than 0')
        self.balance += amount
        if not self.active and self.balance >= 0:
            self.active = True
            self.overdraftCount = 0  
            print('Account reactivated. Overdraft cleared and balance restored.')
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
    
    @staticmethod
    def check_password(password):
        if len(password) < 8:
            return 'Weak'
        if not re.search(r"[A-Za-z]", password):
            return 'Weak'
        if not re.search(r"[0-9]", password):
            return 'Weak'
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            return 'Weak'
        return 'strong'




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
                    if balance_checking is not None and 'checking_active' in row:
                        customer.checking_account.active = row['checking_active'].lower() == 'true'
                    if balance_savings is not None and 'savings_active' in row:
                        customer.savings_account.active = row['savings_active'].lower() == 'true'
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
    
    #11
    def new_account_id(self):
        if self.customers:  
            customer_id = max(map(int,self.customers.keys())) + 1 
            while customer_id in self.customers:  
                customer_id += 1
        else:
            customer_id = 100
            
        return str(customer_id)
    
    
    def add_new_customer(self, fname, lname, password, balance_checking = None, balance_savings = None):
        
        if not fname or not lname or not password:
            raise ValueError("First name, last name, and password are required")
        
        if Customer.check_password(password) == "Weak":
            raise ValueError("Password is weak")
        
        if balance_checking is None and balance_savings is None:
            raise ValueError("At least one account type checking or savings are required")
        
        
        customer_id = self.new_account_id()
        customer = Customer(customer_id, fname, lname, password, balance_checking, balance_savings)
        self.customers[customer_id] = customer
        self.save_customers()
        return customer
    
    
    
    def get_customers(self, customer_id):
        if customer_id not in self.customers:
            raise ValueError(f"The Customer account ID {customer_id} not found") 
        return self.customers.get(customer_id)

    def login_customer(self, customer_id, password): 
        try: 
            customer = self.get_customers(customer_id) 
            if customer.password != password: 
                return None 
            return customer 
        except ValueError: 
            return None

    def transfer(self, sender_id, recipient_id, amount, from_account_type, to_account_type):
        sender = self.get_customers(sender_id)
        recipient = self.get_customers(recipient_id)

        if from_account_type == 'checking' and sender.has_checking():
            sender_account = sender.checking_account
        elif from_account_type == 'savings' and sender.has_savings():
            sender_account = sender.savings_account
        else:
            return 'Sender account type not available.'

        if to_account_type == 'checking' and recipient.has_checking():
            recipient_account = recipient.checking_account
        elif to_account_type == 'savings' and recipient.has_savings():
            recipient_account = recipient.savings_account
        else:
            return 'Recipient account type not available.'

        if sender_account.balance >= amount:
            sender_account.withdraw(amount)
            recipient_account.deposit(amount)
            self.save_customers()
            return f'{amount} has been transferred to ID {recipient_id}. Updated balance: {sender_account.balance}'
        else:
            return 'Low funds'

        
        


