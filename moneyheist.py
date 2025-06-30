
# a function to create a new user

def createAccount():
    
    with open('data.txt','a') as f:
        accountNumber = input("Enter the account number: ")
        userName = input("Enter a username: ")
        balance = input("Deposit some initial amoumt: ")
        f.write(f'{accountNumber},{userName},{balance}\n')
        print("Account created successfully")

# a function to deposit money
#funtion to cheak the validity of the account
def viewAccount(accno):
    with open("data.txt", 'r') as f:
        for line in f:
            parts = line.strip().split(',')
            if len(parts) != 3:
                continue  # Skip blank or malformed lines
            accountNumber, userName, balance = parts
            if accno == accountNumber:
                return [accountNumber, userName, float(balance)]
    return None

                
    
# create a function to update the data in case of any actions


    
# def updateAccount(accno, newBalance):
    
#     with open('data.txt','r') as f:
#         lines = []
#         for line in f:
#             accountNumber, userName, amount = line.strip().split(',')
#             if accno == accountNumber:

#                 lines.append(f'{accountNumber},{userName},{newBalance}')
#             else:
#                 lines.append(line.strip())

#     with open('data.txt','w') as f:
#             f.writelines(lines)

def updateAccount(accno, newBalance):
    lines = []
    with open('data.txt','r') as f:
        for line in f:
            parts = line.strip().split(',')
            if len(parts) != 3:
                continue  # Skip malformed lines
            accountNumber, userName, amount = parts
            if accno == accountNumber:
                lines.append(f'{accountNumber},{userName},{newBalance}\n')
            else:
                lines.append(f'{accountNumber},{userName},{amount}\n')

    with open('data.txt','w') as f:
        f.writelines(lines)


    
def deposit():
    accno = input('Enter the account number: ')
    accountNumber = viewAccount(accno)
    if accountNumber:
        amount =float(input("Enter  the amount: "))
        updateAccount(accno, accountNumber[2] + amount)
        print("Deposit successful")
    else:
        print("The Account not found")

def withdraw():
    accno = input("enter the account number: ")
    accountNumber = viewAccount(accno)
    if accountNumber :

        amount = float(input ("enter the amount to widthraw: "))
        if accountNumber[2] >= amount:
            
            updateAccount(accno, accountNumber[2] - amount )
        else:
            print("The amount is insufficient")
    else:
        print ("There is no account of this kind")
        print ("Try creating a new account")

# def check():
#     accno = input("Enter the your account number: ")
#     accountNumber = viewAccount(accno)

#     with open ("data.txt", "r") as f:
#         for lines in f:
#             accountNumber, userName, balance = lines.strip().split(",")
#             if accno == accountNumber:                    
#                 print(f"Here is your account details {accountNumber},{userName},{balance}")
#             else:
#                print("The account number isn't recognized")
def check():
    accno = input("Enter your account number: ")
    account = viewAccount(accno)
    if account:
        print(f"Here is your account details: {account[0]}, {account[1]}, Balance: {account[2]}")
    else:
        print("The account number isn't recognized.")


#security extention


while True:
    print ("Enter the ultimate choice")
    options = ('1.createAccount','2. deposit','3. withdraw','4. cheakAccount','5. exit')
    print(options)
    userInput  = input(f"Enter (1,2,3,4,5) : ")  
 
    if userInput == '1':
        createAccount()
    elif userInput == '2':
        deposit()
    elif userInput == '3':
        withdraw()
    elif userInput == '4':
        check()
    elif userInput == '5': 
        break
    else : print("hello ther this seams to be an error")
