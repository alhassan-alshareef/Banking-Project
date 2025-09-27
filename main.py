from users.users import Bank, Customer


class BankAPP:
    def __init__(self, bank):
        self.bank = bank
        self.user = None

    def login(self):
        customer_id = input("🆔 Please Enter your account ID: ")
        password = input("🔑 Please Enter your password: ")
        customer = self.bank.login_customer(customer_id, password)
        
        if customer:
            self.user = customer
            print(f"\n🎉 Welcome {customer.Fname} {customer.Lname}!")
            return True
        else:
            print("❌ Invalid customer ID or password")
            return False

    def run(self):
        while True:
            if not self.user:
                print("\nA. 📝 Log in to your account")
                print("B. ➕ Add a new customer")
                print("C. ❌ Exit the program")
                action = input("\nChoose an action: ").lower()
                
                if action == 'a':
                    self.login()
                    
                    
                    
                elif action == 'b':
                    fname = input("👤 First Name: ")
                    lname = input("👤 Last Name: ")
                    while True:
                        password = input("🔑 Password: ")
                        try:
                            if Customer.check_password(password) == "Weak":
                                raise ValueError("Password is weak")
                            break
                        except ValueError as e:
                            print("❌ Error:", e)
                            
                    print("\nChoose account type to open:")
                    print("1. 💳 Checking")
                    print("2. 🏦 Savings")
                    print("3. 💳🏦 Both")
                    choice = input("➡ Enter choice (1-3): ")
                
                    balance_checking = None
                    balance_savings = None
                    
                    while True:
                        if choice in ['1', '3']:
                            checking = input("💵 Initial Checking balance (or leave empty): ")
                            balance_checking = float(checking) if checking else 0
                        
                        if choice in ['2', '3']:
                            savings = input("💰 Initial Savings balance (or leave empty): ")
                            balance_savings = float(savings) if savings else 0
                        try:
                            customer = self.bank.add_new_customer(fname, lname, password, balance_checking, balance_savings)
                            print(f"✅ Customer created! ID: {customer.customer_id}")
                            if customer.has_checking():
                                print(f"Checking account balance: ${customer.checking_account.balance}")
                            if customer.has_savings():
                                print(f"Savings account balance: ${customer.savings_account.balance}")
                            break
                        except ValueError as e:
                            print("❌ Error:", e)
                            
                            
                elif action == 'c':
                    print("👋 Goodbye!")
                    break
                
                
                else:
                    print("❌ Invalid option")
                    


def main():
    print("🌟 Welcome to ACME Bank 🌟")
    bank = Bank("banck.csv")
    app = BankAPP(bank)
    app.run()


if __name__ == "__main__":
    main()
