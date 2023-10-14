
class Bank:
    def __init__(self,name) -> None:
        self.name = name
        self.loan_status = None
        self._bankBalance = 0
        self._givenLoan = 0 
    def total_balance(self):
        print(f"TOTAL BALANCE IN THE BANK : {self._bankBalance}")
        
class Admin:
    def __init__(self,name,email,password,bank) -> None:
        self.name = name
        self.email = email
        self.password = password
        self.id = {len(Account.accounts)+2325}
    
    def delete_user(self,acc_no):
        flag = False
        for account in Account.accounts:
            if account.acc_no == acc_no:
                Account.accounts.remove(account)
                flag = True 
                break
        
        if flag:
            print(f"Acc No : {acc_no} deleted successfully")
    def add_money(self,amount,bank):
        if amount > 0:
            bank._bankBalance+=amount
            print(f"${amount} added in the bank")
        else:
            print("successfully failed to add money")
    def all_user(self):
        print("----OUR USERS-----")
        for user in Account.accounts:
            
            print(user)
            print('-----------------\n')
    
    def loan_modify(self,bank,loanStatus):
        bank.loan_status = loanStatus


class Account:
    accounts = []
    def __init__(self,name,email,address,account_type) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.loan_count = 0
        self.deposit_transaction = {}
        self.withdraw_transaction = {}
        self.acc_no = f"{len(self.accounts)+7877}"
        self.deposit_transaction[self.acc_no] = []
        self.withdraw_transaction[self.acc_no] = []
        Account.accounts.append(self)
    

    def deposit(self,amount,bank):
        if(amount>0):
            self.balance += amount
            bank._bankBalance += amount
            print(f"-------${amount} Deposit successful-------")
            
            self.deposit_transaction[self.acc_no].append(amount)
        else:
            print("\n--Invalid amount--\n")
    
    def withdraw(self,amount,bank):
        if(amount>0 and self.balance >= amount):
            self.balance -= amount 
            bank._bankBalance -= amount
            print(f"--------${amount} Withdraw successful-------")
            
            self.withdraw_transaction[self.acc_no].append(amount)
        elif self.balance < amount:
            print("\n--Withdrawal amount exceeded--\n")

        else : 
            print("\n--Invalid amount--\n")
    def update_info(self,name):
        self.name = name
    def update_info(self,name,address):
        self.name = name
        self.address = address
    
    def transaction_history(self,account_no):
        for key,val in self.deposit_transaction.items():
            if key == account_no:
                print("--Deposit transaction history--")
                for item in val:
                    print(f"            +{item}")
            else: 
                print("--No Deposit Transaction Found--")

        for key,val in self.withdraw_transaction.items():
            if key == account_no:
                print("--Withdraw Transaction History--")
                for item in val:
                    print(f"            -{item}")
            else: 
                print("--No Withdraw Transaction Found--")

    def take_loan(self,amount,bank):
        if bank.loan_status:
            if self.loan_count<2:
                if bank._bankBalance > amount:
                    self.loan_count += 1
                    bank._givenLoan+=amount
                    self.balance += amount
                    bank._bankBalance -= amount
                    print(f"You've got loan ${amount}. {2- self.loan_count} more loan left.")
                else :
                    print("You're not eligible for loan.")
        else:
            print("No loan services are available")
    def transfer_balance(self,acc_no,amount):
        flag = False
        for account in self.accounts:
            if acc_no == account.acc_no:
                if self.balance >= amount:
                    account.balance += amount
                    self.balance -= amount
                    flag = True
                    break
        
        if flag:
            print(f"${amount} Transfered successfully to Account No : {acc_no}")
        else :
            print(f"Account does not exist")

    @property
    def check_balance(self):
        print(f"Current Balance : {self.balance}")

    def __repr__(self) -> str:
        print(f"Name : {self.name}\nAccount No : {self.acc_no}\nBalance : {self.balance}")
        return ''
class SavingsAccount(Account):
    def __init__(self, name, email, address) -> None:
        super().__init__(name, email, address,"Savings")
    
   


class SpecialAccount(Account):
    def __init__(self, name, email, address) -> None:
        super().__init__(name, email, address,"Special")
        

    
    def show_info(self):
        print(f"\n--------ACCOUNT INFO------------\n")
        print(f"Name : {self.name}\nAccount No : {self.acc_number}\nAccount Type : {self.account_type}\bBalance : {self.balance}")



current_user = None
current_admin = None
sonali = Bank('SONALI BANK')
while True:
   
    op = input("1. User Account\n2. Admin Account\n")
    if op =='1':
        if current_user == None:
            print("\n-----No user Logged in------\n")
            ch = input("\nLog in or Register(L/R) : ")
            if ch == 'R':
                name = input("Name : ")
                email = input("Email : ")
                address = input("Address : ")

                acc_choose = input("Account type :\n1. Savings\n2. Special\n")
                if acc_choose =='1':

                    user = SavingsAccount(name,email,address)
                    current_user = user
                elif acc_choose == '2':
                    user = SpecialAccount(name,email,address)
                    current_user = user
                else:
                    print("Invalid input\n")
                

            elif ch == 'L':
                mail = input("Enter your email : ")
                flag = False
                for account in Account.accounts:
                    if account.email == mail:
                        current_user = account
                        break
                    
        else: 

            if current_user:
                print(f"\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Transfer balance\n5. Take loan\n6. Log Out")
                ch = input()
                if ch =='1':
                    amount = int(input("Enter amount : "))
                    current_user.deposit(amount,sonali)
                elif ch == '2':
                    amount = int(input("Enter amount : "))
                    current_user.withdraw(amount,sonali)
                elif ch == '3':
                    print(f"Current Balance : {current_user.balance}\n")

                elif ch == '4':
                   account_no = input("Enter the account Number : ")
                   amount = int(input("Enter amount : "))
                   current_user.transfer_balance(account_no,amount)
                elif ch == '5':
                    amount = int(input("Enter amount: "))
                    current_user.take_loan(amount,sonali)
                elif ch == '6':
                    current_user = None
    
    elif op =='2':
        if current_admin == None:
            print("-----Admin Login-------")
            name = input("Name : ")
            email = input("Email : ")
            password = input("Password : ")
            admin = Admin(name,email,password,sonali)
            current_admin = admin
        
        else:
            if current_admin:
                print(f"\n1. Delete User\n2. All accounts\n3. Total balance \n4. Total Loan\n5. Loan Modification\n6. Log Out")
                ch = input()
                if ch =='1':
                    account_number = input("Enter amount : ")
                    current_admin.delete_user(account_number)
                elif ch == '2':
                    current_admin.all_user()
                elif ch == '3':
                    print(f"Total balance in the bank : {sonali._bankBalance}")

                elif ch == '4':
                  print(f"Total Given Loan : {sonali._givenLoan}")
                elif ch == '5':
                    loan_check = input("1. Loan on\n2. Loan off\n")
                    if loan_check =='1':
                        current_admin.loan_modify(sonali,"on")
                    elif loan_check=='2':
                        current_admin.loan_modify(sonali,'')
                elif ch == '6':
                    current_admin = None