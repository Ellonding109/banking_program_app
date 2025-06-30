
# a function to create a new user

def createAccount():
    
    with open('data.txt','a') as f:
<<<<<<< HEAD
        accountNumber = input("Enter the account number: ")
=======
        accountNumber = input("Enter the account account number: ")
>>>>>>> ec4c8d79d9436d1448fe989d43860d6f8fe20db8
        userName = input("Enter a username: ")
        balance = input("Deposit some initial amoumt: ")
        f.write(f'{accountNumber},{userName},{balance}\n')
        print("Account created successfully")

# a function to deposit money
#funtion to cheak the validity of the account
def viewAccount(accno):
<<<<<<< HEAD
    with open("data.txt", 'r') as f:
        for line in f:
            parts = line.strip().split(',')
            if len(parts) != 3:
                continue  # Skip blank or malformed lines
            accountNumber, userName, balance = parts
            if accno == accountNumber:
                return [accountNumber, userName, float(balance)]
    return None
=======
        with open("data.txt",'r') as f:
            for lines in f:
                accountNumber, userName, balance = lines.strip().split(',')
                if accno == accountNumber:

                    return[accountNumber,userName,float(balance)]
                else:
                    print("there do not exixt such an account")
>>>>>>> ec4c8d79d9436d1448fe989d43860d6f8fe20db8

                
    
# create a function to update the data in case of any actions


    
<<<<<<< HEAD
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

=======
def updateAccount(accno, newBalance):
    lines = []
    with open('data.txt', 'r') as f:
        for line in f:
            accountNumber, userName, amount = line.strip().split(',')
            if accno == accountNumber:

                lines.append(f'{accountNumber},{userName},{newBalance}')
            else:
                lines.append(lines)

    with open('data.txt','w') as f:
            f.writelines(lines)
>>>>>>> ec4c8d79d9436d1448fe989d43860d6f8fe20db8

    
def deposit():
    accno = input('Enter the account number: ')
    accountNumber = viewAccount(accno)
    if accountNumber:
        amount =float(input("Enter  the amount: "))
        updateAccount(accno, accountNumber[2] + amount)
        print("Deposit successful")
    else:
        print("The Account not found")

<<<<<<< HEAD
def withdraw():
=======
def widthraw():
>>>>>>> ec4c8d79d9436d1448fe989d43860d6f8fe20db8
    accno = input("enter the account number: ")
    accountNumber = viewAccount(accno)
    if accountNumber :

        amount = float(input ("enter the amount to widthraw: "))
        if accountNumber[2] >= amount:
            
            updateAccount(accno, accountNumber[2] - amount )
        else:
<<<<<<< HEAD
            print("The amount is insufficient")
=======
            print("The amount is unsufusient go try stilling some more")
>>>>>>> ec4c8d79d9436d1448fe989d43860d6f8fe20db8
    else:
        print ("There is no account of this kind")
        print ("Try creating a new account")

<<<<<<< HEAD
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

=======
def check():
    accno = input("Enter the your account number: ")
    accountNumber = viewAccount(accno)

    with open ("data.txt", "r") as f:
        for lines in f:
            accountNumber, userName, balance = lines.strip().split(",")
            if accno == accountNumber:                    
                print(f"Here is your account details {accountNumber},{userName},{balance}")
            else:
               print("The account number isn't recognized")
>>>>>>> ec4c8d79d9436d1448fe989d43860d6f8fe20db8

#security extention


while True:
    print ("Enter the ultimate choice")
<<<<<<< HEAD
    options = ('1.createAccount','2. deposit','3. withdraw','4. cheakAccount','5. exit')
=======
    options = ('1.deposit','2. widthraw','3. createAccount','4. cheakAccount','5. exit')
>>>>>>> ec4c8d79d9436d1448fe989d43860d6f8fe20db8
    print(options)
    userInput  = input(f"Enter (1,2,3,4,5) : ")  
 
    if userInput == '1':
<<<<<<< HEAD
        createAccount()
    elif userInput == '2':
        deposit()
    elif userInput == '3':
        withdraw()
=======
        deposit()
    elif userInput == '2':
        widthraw()
    elif userInput == '3':
        createAccount()
>>>>>>> ec4c8d79d9436d1448fe989d43860d6f8fe20db8
    elif userInput == '4':
        check()
    elif userInput == '5': 
        break
<<<<<<< HEAD
    else : print("hello ther this seams to be an error")
=======
    #else : print("hello ther this seams to be an error")
>>>>>>> ec4c8d79d9436d1448fe989d43860d6f8fe20db8
