# Bank Project

## Overview

This is a simple bank application that allows customers to manage their accounts. Customers can:

- 💵 Deposit and withdraw money
- 🔄 Transfer money between their accounts or to other customers
- ⚠️ Handle overdraft situations safely

The project is written in **Python** and focuses on security and user-friendly features.

##
## Features ✅

 🧑‍💻 User Login and Registration
- Secure login and the ability to create a new account.

 🏦 Checking and Savings Accounts
- Support for checking and savings accounts for each user.

 ⚠️ Overdraft Protection
- Protects accounts from overdraft:
  - Charges $35 if the balance goes below zero.
  - Deactivates the account after two overdrafts.

 ♻️ Account Reactivation
- Deposit money to reactivate inactive accounts.

 💸 Money Transfer
- Transfer money between accounts of the same user or between different users.

 🆔 Unique Account ID
- Generates a unique ID for each account to prevent duplication.

##

# 💻 Code I’m Proud Of

## 🆔 Unique Account ID Generation



```python
def new_account_id(self):
    if self.customers:  
        customer_id = max(map(int, self.customers.keys())) + 1
        while customer_id in self.customers:
            customer_id += 1
    else:
        customer_id = 100
    return str(customer_id)
```

##💸 Withdraw & Deposit with Overdraft Handling

```python
def withdraw(self, amount):
    if not self.active:
        raise ValueError('Account is deactivated')
    if amount <= 0:
        raise ValueError('Withdrawal amount must be greater than 0')
    new_balance = self.balance - amount
    if new_balance < -100:
        raise ValueError("Account cannot have a resulting balance of less than -$100.")
    self.balance = new_balance
    if self.balance < 0:
        self.balance -= 35
        self.overdraftCount += 1
        print('Overdraft occurred — $35 fee added to your balance.')
        if self.overdraftCount >= 2:
            self.active = False
            print('Account has been deactivated')
    return self.balance

def deposit(self, amount):
    if amount <= 0:
        raise ValueError('The amount must be greater than 0')
    self.balance += amount
    if not self.active and self.balance >= 0:
        self.active = True
        self.overdraftCount = 0
        print('Account reactivated. Overdraft cleared and balance restored.')
    return self.balance

```



