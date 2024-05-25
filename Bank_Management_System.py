#Admin password: Sonali123
#first_admin=Admin_Account("Rahim","rahim@gmail.com","Dhaka")
class User:
    def __init__(self,name,email,address,account_type):
        self.name=name
        self.email=email
        self.address=address
        self.account_type=account_type
        self.__password=input("Set your password: ")
        self.balance=0
        self.account_number=self.name+self.email
        self.transactions_list=[]
        self.loan_count=0
        self.total_loan_payable=0
        print(f"Congrats the account has been created. The account number is {self.account_number}")

    def password(self):
        return self.__password
    
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"Tk. {amount} has been deposited successfully by {self.name}. Current balance: Tk. {self.balance}")
            s=f"Deposit: Tk. {amount} Current Balance: Tk. {self.balance}"
            self.transactions_list.append(s)
        else:
            print("Invalid amount. Amount of deposit can not be 0 or negative.")
        
    def withdraw(self,bank,amount):
        if bank.is_bankrupt()==False:
            if amount>0:
                if amount<self.balance:
                    self.balance-=amount
                    print(f"Tk. {amount} has been withdrawn successfully. Current balance: Tk. {self.balance}")
                    s=f"Withdraw: Tk. {amount} Current Balance: Tk. {self.balance}"
                    self.transactions_list.append(s)
                else:
                    print(f"Withdrawal amount exceeded. You can not withdraw more than Tk. {self.balance}")
            else:
                print("Invalid amount. Amount of withdrawal can not be 0 or negative.")
        else:
            print("We are extremely sorry to inform you that our bank has gone bankrupt. You can not withdraw money.")

    def check_balance(self):
        print(f"Your current balance: Tk. {self.balance}")
    
    def show_transaction_history(self):
        print(f"Transaction history of {self.name} (Account Number: {self.account_number}):")
        for trxn in self.transactions_list:
            print(trxn)
    
    def take_loan(self,bank,amount):
        if bank.loan_feature() and self.loan_count<2:
            if amount>0:
                self.loan_count+=1
                self.balance+=amount
                self.total_loan_payable+=amount
                print(f"You have taken a loan of Tk. {amount}. Current Balance: Tk. {self.balance}")
                s=f"Loan: Tk. {amount} Current Balance: Tk. {self.balance}"
                self.transactions_list.append(s)
            else:
                print("Invalid loan request. Loan can not be zero or negative")
        elif bank.loan_feature()==False:
            print("Our Apologies. The bank is currently not disbursing any loans")
        elif self.loan_count==2:
            print("You can not take more than two loans")
    
    def money_transfer(self,recipient_id,amount,bank):
        flag=False
        recipient=None
        for user in bank.user_accounts_list:
            if user.account_number==recipient_id:
                recipient=user
                flag=True
                break
        if flag==True:
            if self.balance>=amount:
                self.balance-=amount
                recipient.balance+=amount
                print(f"Tk. {amount} has been transferred from Account {self.account_number} to Account {recipient.account_number} successfully.")
                s=f"Transfer money to: {recipient.name}({recipient_id}) Amount: Tk. {amount} Current Balance: Tk. {self.balance}"
                self.transactions_list.append(s)   
            else:
                print("Not enough money to make transfer")

        else:
            print("Recipient Account does not exist")
        
class Bank:#This class will do all the work of admins
    def __init__(self,bank_name):
        self.bank_name=bank_name
        self.__total_balance=0
        self.__total_loan_disbursed=0
        self.user_accounts_list=[]
        self.admin_accounts_list=[]
        self.__bankruptcy=False
        self.__loan_feature=True
    def create_user_account(self):
        user_name=input("New User name: ")
        user_email=input("New User email: ")
        flag=True
        for i in self.user_accounts_list:
            if user_name.lower()==i.name.lower() and user_email.lower()==i.email.lower():
                flag=False
                break
        if flag==False:
            print("Account is already created.")
        else:
            user_address=input("New User address: ")
            user_account_type=input("User account type('C' for Current and 'S' for Savings): ")
            if user_account_type!='C' and user_account_type!='S':
                print("Invalid account type")
                return
            user=User(user_name,user_email,user_address,user_account_type)
            self.user_accounts_list.append(user)
    def create_admin_account(self):
        name=input("New Admin Name: ")
        email=input("New Admin Email: ")
        address=input("New Admin Address: ")
        admin=Admin_Account(name,email,address)
        self.admin_accounts_list.append(admin)
    def delete_user_account(self,user):
        self.user_accounts_list.remove(user)
    def show_user_account_list(self):
        print("*******All Users*******")
        for user in self.user_accounts_list:
            print(f"User name: {user.name} User account number: {user.account_number} User balance: {user.balance}")
    def bankrupt(self):
        self.__bankruptcy=True
    def is_bankrupt(self):
        return self.__bankruptcy
    def total_balance(self):
        self.__total_balance=0
        for user in self.user_accounts_list:
            self.__total_balance+=user.balance
        print("Total available balance: ",self.__total_balance)
    def on_loan_feature(self):
        self.__loan_feature=True
    def off_loan_feature(self):
        self.__loan_feature=False
    def loan_feature(self):
        return self.__loan_feature
    def total_loan(self):
        self.__total_loan_disbursed=0
        for user in self.user_accounts_list:
            self.__total_loan_disbursed+=user.total_loan_payable
        print("Total loan amount: ",self.__total_loan_disbursed)
    
class Admin_Account():
    def __init__(self, name, email, address):
        self.name=name
        self.email=email
        self.address=address

sonali=Bank("Sonali Bank PLC")
first_admin=Admin_Account("Rahim","rahim@gmail.com","Dhaka")#Admin corner must be accessed firstly using these credentials
sonali.admin_accounts_list.append(first_admin)
print("Welcome to Sonali Bank PLC")
while True:
    print("1. User")
    print("2. Admin")
    print("3. Exit")
    op=input("Enter command: ")
    if op=="1":
        user=None
        print("1. Log in")
        print("2. Make an account")
        print("Press any other key for Exit")
        op_account=input("Enter Command: ")
        if op_account=="1":
            name=input("Enter your name: ")
            password=input("Enter your password: ")
            flag=False
            for i in sonali.user_accounts_list:
                if i.name.lower()==name.lower() and i.password()==password:
                    user=i
                    flag=True
                    break
            if flag==False:
                print("Username and password do not match. Try again.")
                continue
        elif op_account=="2":
            sonali.create_user_account()
            continue
        else:
            continue
        while True:
            print(f"Welcome {user.name}. Select one of the following options: ")
            print("1. Deposit Money")
            print("2. Withdraw Money")
            print("3. Check Bank Balance")
            print("4. Check Transaction History")
            print("5. Take Loan")
            print("6. Transfer Money")
            print("7. Exit")
            op_user=input("Enter Command: ")
            if op_user=="1":
                amount=int(input("Enter the amount of deposit: "))
                user.deposit(amount)
            elif op_user=="2":
                amount=int(input("Enter the amount of withdrawal: "))
                user.withdraw(sonali,amount)
            elif op_user=="3":
                user.check_balance()
            elif op_user=="4":
                user.show_transaction_history()
            elif op_user=="5":
                amount=int(input("Enter the amount of loan: "))
                user.take_loan(sonali,amount)
            elif op_user=="6":
                amount=int(input("Enter the amount that you want to transfer: "))
                recipient=input("Enter Account Number of the Recipient: ")
                user.money_transfer(recipient,amount,sonali)
            elif op_user=="7":
                break
            else:
                print("Invalid Command")
    elif op=="2":
        name=input("Enter Name: ")
        email=input("Enter Email: ")
        flag=False
        for admin in sonali.admin_accounts_list:
            if admin.name.lower()==name.lower() and admin.email.lower()==email.lower():
                flag=True
                break
        password=input("Enter password: ")
        if password=="Sonali123" and flag==True:
            while True:
                print("Welcome Admin. What do you want to do?")
                print("1. Create User Account")
                print("2. Create Admin Account")
                print("3. Delete User Account")
                print("4. See List of User Accounts")
                print("5. Check Total Available Balance")
                print("6. Check Total Loan Amount")
                print("7. Enable or Disable Loan Feature")
                print("8. Declare Bankruptcy")
                print("9. Exit")
                op_admin=input("Enter comamnd: ")
                if op_admin=="1":
                    sonali.create_user_account()
                elif op_admin=="2":
                    sonali.create_admin_account()
                    print("Admin account has been created")
                elif op_admin=="3":
                    print("Deleting User: ")
                    dlt_name=input("Enter the name of the user: ")
                    dlt_email=input("Enter the email of the user: ")
                    flag=True
                    for i in sonali.user_accounts_list:
                        if i.name.lower()==dlt_name.lower() and i.email.lower()==dlt_email.lower():
                            flag=False
                            sonali.delete_user_account(i)
                            print("The account has been deleted")
                            break
                    if flag==True:
                        print("User does not exist")
                elif op_admin=="4":
                    sonali.show_user_account_list()
                elif op_admin=="5":
                    sonali.total_balance()
                elif op_admin=="6":
                    sonali.total_loan()
                elif op_admin=="7":
                    print("1. Enable Loan Feature")
                    print("2. Disable Loan Feature")
                    x=input("Enter Command: ")
                    if x=="1":
                        sonali.on_loan_feature()
                        print("Loan feature has been turned on")
                    elif x=="2":
                        sonali.off_loan_feature()
                        print("Loan feature has been turned off")
                    else:
                        print("Invalid Command")
                elif op_admin=="8":
                    sonali.bankrupt()
                    sonali.off_loan_feature()
                    print("The bank has gone bankrupt")
                elif op_admin=="9":
                    break
        else:
            print("Unauthorized entry")
    elif op=="3":
        break
    else:
        print("Invalid Command")