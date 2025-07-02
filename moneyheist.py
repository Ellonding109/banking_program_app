
# a function to create a new user

def createAccount():
    
    with open('data.txt','a') as f:
        accountNumber = input("Enter the account account number: ")
        userName = input("Enter a username: ")
        secretkey = input("Enter a password: ")
        secretkey1 = input("Reenter the password: ")
        
        if secretkey != secretkey1:
            print ("the password aren't same")
            return createAccount()
        
        balance = input("Deposit some initial amoumt: ")
        
        f.write(f'{accountNumber},{userName},{secretkey},{balance}\n')
        print("Account created successfully")

#a function to impliment the cheaking of the password
def security(key): 
    with open("data.txt","r") as f:
        for lines in f:
            accountNumber, userName, secretkey, balance = lines.strip().split(',')
            if key == secretkey:

                return[accountNumber,userName,secretkey,float(balance)]
            
            else:
                print("The password is incorrect")


#funtion to cheak the validity of the account
def viewAccount(accno):
        with open("data.txt",'r') as f:
            for lines in f:
                accountNumber, userName, secretkey, balance = lines.strip().split(',')
                if accno == accountNumber:

                    return[accountNumber,userName,float(balance)]
                
                else:
                    print("The account number is nor valid")


# create a function to update the data in case of any actions
 
def updateAccount(accno, newBalance):
    lines = []
    with open('data.txt', 'r') as f:
        for line in f:
            accountNumber, userName, secretkey, amount = line.strip().split(',')
            if accno == accountNumber:

                lines.append(f'{accountNumber},{userName},{secretkey},{newBalance}')
            else:
                lines.append(lines)

    with open('data.txt','w') as f:
            f.writelines(lines)

    
def deposit():
    
    accno = input('Enter the account number: ')
    key = input('Enter your password: ')
    accountNumber = viewAccount(accno)
    secretkey = security(key)
    if accountNumber and secretkey:
        amount =float(input("Enter  the amount: "))
        updateAccount(accno, accountNumber[2] + amount)
        print("Deposit successful")
    else:
        print("The Account not found")

def widthraw():
    accno = input("enter the account number: ")
    key = input('Enter your password: ')
    accountNumber = viewAccount(accno)
    secretkey = security(key)
    if accountNumber and secretkey:

        amount = float(input ("enter the amount to widthraw: "))
        if accountNumber[2] <= 0:
            print ('Top up to your account to make a withdraw action')
        else:
            return accountNumber[2]

        if accountNumber[2] >= amount:
            
            updateAccount(accno, accountNumber[2] - amount )

        else:

            print("The amount is unsufusient please topup to you account")

    else:
        print ("this account does not exist")
        print ("Try creating a new account")

def check():
    accno = input("Enter the your account number: ")
    key = input("Enter you password: ")
    accountNumber = viewAccount(accno)
    secretkey = security(key)
    

    with open ("data.txt", "r") as f:
        for lines in f:
            accountNumber, userName, secretkey, balance = lines.strip().split(",")
            if accno == accountNumber and key == secretkey:         

                print(f"Here is your account details {accountNumber},{userName},{balance}")
            else:
               
               print("Either the account number or password isn't recognized")

while True:
    print ("Enter the ultimate choice")
    options = ('1.deposit','2. widthraw','3. createAccount','4. cheakAccount','5. exit')
    print(options)
    userInput  = input(f"Enter (1,2,3,4,5) : ")  
 
    if userInput == '1':
        deposit()
    elif userInput == '2':
        widthraw()
    elif userInput == '3':
        createAccount()
    elif userInput == '4':
        check()
    elif userInput == '5': 
        break
    else : print("hello ther this seams to be an error")
