import os

#file
# file = open("kwoba.txt","x")
# file.close()
# # Main Menu
def menu():
    while True:
        print("\n=== Simple Banking System ===")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. View Account")
        print("5. Find account")
        print("6. Exit")

        choice = input("Select option (1-6): ")

        if choice == '1':
            createAccount()
        elif choice == '2':
            deposit()
        elif choice == '3':
            withdraw()
        elif choice == '5':
            findAccount()
        elif choice == '4':
        
            viewAccount()
        elif choice == '6':
            print("👋 Exiting program. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")
def createAccount():
    print("Create an account with us")
    accno = input("Enter an account number: ")
    name = input("Enter your name: ")
    balance = input("Enter an initial deposit: ")
    with open ("account.txt","a") as f:
        f.write(f"{accno}, {name}, {balance}\n")
    print("Account created successfuly")
def findAccount():
    details = createAccount()
    accnumber = input("Enter the account no: ")
  

    if not os.path.exists("account.txt"):
        print("You need to create an account!")
    elif accnumber == details:
        with open("account.txt") as f:
            print(f.read())
    
def deposit():
    acc = findAccount()
    print("Enter the amount you want to deposit: ")
    accno = ("Enter your account number :")
    amount = input("Enter the amount to add: ")
    


def withdraw():
    pass
def viewAccount():
    pass



# Run the program
menu()

