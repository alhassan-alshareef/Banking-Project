def main():
    while True:
        print("Welcome to the Banking System!")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            create_account()
        elif choice == '2':
            login()
        elif choice == '3':
            print("Thank you for using the Banking System. Goodbye!")
            break
        else:
            print("Invalid input. Please try again.\n")