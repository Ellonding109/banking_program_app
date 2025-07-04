def createAccount():
    with open('data.txt', 'a') as f:
        accountNumber = input("Enter the account number: ")
        userName = input("Enter a username: ")
        secretkey = input("Enter a password: ")
        secretkey1 = input("Reenter the password: ")

        while secretkey != secretkey1:
            print("The passwords don't match. Try again.")
            secretkey = input("Enter a password: ")
            secretkey1 = input("Reenter the password: ")

        balance = input("Deposit some initial amount: ")
        f.write(f'{accountNumber},{userName},{secretkey},{balance}\n')
        print("Account created successfully")


def security(key):
    with open("data.txt", "r") as f:
        for line in f:
            accountNumber, userName, secretkey, balance = line.strip().split(',')
            if key == secretkey:
                return [accountNumber, userName, secretkey, float(balance)]
    print("The password is incorrect")
    return None


def viewAccount(accno):
    with open("data.txt", 'r') as f:
        for line in f:
            accountNumber, userName, secretkey, balance = line.strip().split(',')
            if accno == accountNumber:
                return [accountNumber, userName, secretkey, float(balance)]
    print("The account number is not valid")
    return None


def updateAccount(accno, newBalance):
    lines = []
    with open('data.txt', 'r') as f:
        for line in f:
            accountNumber, userName, secretkey, amount = line.strip().split(',')
            if accno == accountNumber:
                lines.append(f'{accountNumber},{userName},{secretkey},{newBalance}\n')
            else:
                lines.append(line)

    with open('data.txt', 'w') as f:
        f.writelines(lines)


def deposit():
    accno = input('Enter the account number: ')
    key = input('Enter your password: ')
    account = viewAccount(accno)
    auth = security(key)

    if account and auth and account[2] == key:
        amount = float(input("Enter the amount to deposit: "))
        updateAccount(accno, account[3] + amount)
        print("Deposit successful")
    else:
        print("Account not found or password incorrect.")


def withdraw():
    accno = input("Enter the account number: ")
    key = input('Enter your password: ')
    account = viewAccount(accno)
    auth = security(key)

    if account and auth and account[2] == key:
        amount = float(input("Enter the amount to withdraw: "))
        if account[3] <= 0:
            print('Top up your account to make a withdrawal.')
        elif account[3] >= amount:
            updateAccount(accno, account[3] - amount)
            print("Withdrawal successful")
        else:
            print("Insufficient funds. Please top up your account.")
    else:
        print("Account not found or password incorrect.")


def check():
    accno = input("Enter your account number: ")
    key = input("Enter your password: ")
    account = viewAccount(accno)
    auth = security(key)

    if account and auth and account[2] == key:
        print(f"Account Number: {account[0]}")
        print(f"Username: {account[1]}")
        print(f"Balance: {account[3]}")
    else:
        print("Account not found or password incorrect.")


# === MAIN MENU LOOP ===
while True:
    print("\n=== Menu ===")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Create Account")
    print("4. View Account")
    print("5. Exit")

    userInput = input("Enter your choice (1-5): ")

    if userInput == '1':
        deposit()
    elif userInput == '2':
        withdraw()
    elif userInput == '3':
        createAccount()
    elif userInput == '4':
        check()
    elif userInput == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
