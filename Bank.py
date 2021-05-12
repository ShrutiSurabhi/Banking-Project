import pandas as pd
import os
import random
import csv
from Employee import Employee
from Person import Person
from Customer import Customer
from Accounts import Accounts


class Bank:
    
    employee_file = ''
    customer_file = ''
    account_file = ''
    list_employees = []
    list_customers = []
    list_accounts = []
    ACC_SIZE=2
    
    def __init__(self, employee_file , customer_file, account_file):
        self.employee_file = employee_file
        self.customer_file = customer_file
        self.account_file = account_file
        #_______________________
        #self.list_employees = list_employees 
        #self.list_customers = list_customers
        #self.list_accounts = list_accounts
        
     
    def read_data(self):
        
        
        if not os.path.exists(self.employee_file):
            with open(self.employee_file,'w') as file:
                dw = csv.DictWriter(file, delimiter = ',',fieldnames= ["Name", "Address"])
                dw.writeheader()
        df = pd.read_csv(self.employee_file)
        
        for index, row in df.iterrows():
            emp = Employee(index, row["Name"],row["Address"])
            self.list_employees.append(emp)
            
        #-----------------------------------------------------------
        
        if not os.path.exists(self.customer_file):
            with open(self.customer_file,'w') as file:
                dw = csv.DictWriter(file, delimiter = ',',fieldnames= ["Name", "Address","Customer id","Account Number(s)"])
                dw.writeheader()
        df = pd.read_csv(self.customer_file)
        
        for index, row in df.iterrows():
            cus = Customer(index, row["Name"],row["Address"], row["Customer id"], row["Account Number(s)"])
            self.list_customers.append(cus)
        
        #-----------------------------------------------------------
                
        if not os.path.exists(self.account_file):
            with open(self.account_file,'w') as file:
                dw = csv.DictWriter(file, delimiter = ',',fieldnames= ["Customer id", "Account Number", "Type", "Total Amount"])
                dw.writeheader()
        df = pd.read_csv(self.account_file)
        
        for index, row in df.iterrows():
            print(row)
            acc = Accounts(index, row["Customer id"],row["Account Number"], row["Type"], row["Total Amount"])
            self.list_accounts.append(acc)
        
        #-----------------------------------------------------------
        

    def find_customer(self,customer_id):
        if customer_id in self.list_customers:
            return self.list_customers[self.list_customers.index(customer_id)]
        return None

    def create_customer(self, name, address):

        cusid = self.get_unique(2)
        cid = Customer(len(self.list_customers), name, address, cusid, "")
        self.list_customers.append(cid)
        
        return cid 

    def create_account(self, acc_type, deposit, found_customers):

        acc_id = self.get_unique(1)
        acc_obj = Accounts(len(self.list_accounts), found_customers.customer_id, acc_id, acc_type, deposit)
        self.list_accounts.append(acc_obj)
        
        return acc_obj 

    def get_unique(self,option):
        if (option == 1):
            acc_no = random.randint(10**self.ACC_SIZE, (10**self.ACC_SIZE+1)-1)
            while acc_no in self.list_accounts:
                acc_no = random.randint(10**self.ACC_SIZE, (10**self.ACC_SIZE+1)-1)
            return acc_no
        if (option == 2):
            cusid = random.randint(100000, 900000)
            while cusid in self.list_customers:
                cusid = random.randint(100000, 900000)
            return cusid

    def close_bank(self):
    #to close csv file
        df = pd.DataFrame([x.as_dict() for x in self.list_customers])
        df.to_csv(self.customer_file)

        df = pd.DataFrame([x.as_dict() for x in self.list_accounts])
        df.to_csv(self.account_file)


        
        


def customerPortal(bank,found_customer):

    choice = ''
    num = 0
    currency = 0
    while choice != 7:
        
        print("\tPLEASE CHOOSE ONE TO PROCEDE")
        print("\t1. NEW ACCOUNT")
        print("\t2. DEPOSIT AMOUNT")
        print("\t3. WITHDRAW AMOUNT")
        print("\t4. BALANCE ENQUIRY")
        print("\t5. CLOSE AN ACCOUNT")
        print("\t6. MODIFY AN ACCOUNT")
        print("\t7. EXIT")
        print("\tSelect Your Option (1-7) ")

        choice = input("Enter your choice : ")


        if choice == '1':
            #interaction for creating an account        
            
            acc_type = input("Ente the type of account [Current/Saving] : ")
            deposit = int(input("Enter the initial amount ($) (>=500 for Saving and >=1000 for current"))
            acc_obj = bank.create_account(acc_type, deposit, found_customer)
            found_customer.create_account(acc_obj)

        elif choice =='2':
            num = int(input("\tEnter the account No. : "))
            currency = int(input("\tEnter the amount you want to deposit ($) : "))
            depositAndWithdraw(num, currency, 1)

        elif choice == '3':
            num = int(input("\tEnter the account No. : "))
            currency = int(input("\tEnter the amount you want to withdraw ($) : "))
            depositAndWithdraw(num, currency, 2)

        elif choice == '4':
            num = int(input("\tEnter The account No. : "))
            #displaySp(num)

        elif choice == '5':
            num =int(input("\tEnter The account No. : "))
            #deleteAccount(num)

        elif choice == '6':
            num = int(input("\tEnter The account No. : "))
            #modifyAccount(num)

        elif choice == '7':
            print("\tThank you for using bank managemnt system. Have a nice day!")
            break

        else:
            print("Invalid choice")

def employeePortal(bank):


    choice = ''
    num = 0
    while choice != 5:

        print("\tCHOOSE ONE TO PROCEDE")
        print("\t1. NEW ACCOUNT")
        print("\t2. ALL ACCOUNT HOLDERS LIST AND THEIR INFORMATION")
        print("\t3. CLOSE AN ACCOUNT")
        print("\t4. MODIFY AN ACCOUNT")
        print("\t5. EXIT")
        print("\tSelect Your Option (1-5) ")

        ch = input("Enter your choice : ")


        if choice == '1':
            #interaction for creating an account        
            Type = input("Ente the type of account you want [Current/Saving] : ")
            deposit = int(input("Enter the initial amount ($) [>=500 for Saving and >=1000 for current] :"))
            create_account(Type, deposit)

        elif choice =='2':
            print(f"***The details of Account holders***\n{show_accounts_info()}")

        elif choice == '3':
            num =int(input("\tEnter The account No. : "))
            customer.deleteAccount(num)

        elif choice == '4':
            num = int(input("\tEnter The account No. : "))
            customer.modifyAccount(num)

        elif choice == '5':
            print("\tThank you for using the banking system. Have a nice day!")
            break
        else:
            print("Invalid choice")

    



if __name__ == "__main__":    
#start of the program
    
    bank = Bank("C:\\Users\\shrut\\OneDrive\\Desktop\\Banking\\employee_data.csv","C:\\Users\\shrut\\OneDrive\\Desktop\\Banking\\customer_data.csv" , "C:\\Users\\shrut\\OneDrive\\Desktop\\Banking\\account_data.csv" )
    bank.read_data()
    cusid = 0 
    #the first interaction to know if the user is employee or customer
    ch =''
    choice = ''
    while (ch!=3):

        print("\t\t\t\t********************************************")
        print("\t\t\t\t\tWELCOME TO THE BANKING SYSTEM")
        print("\t\t\t\t********************************************") 
        print("\tMAIN MENU\n")
        print("\t1. CUSTOMER PORTAL")
        print("\t2. EMPLOYEE PORTAL")
        print("\t3. EXIT")
        print("\tSelect Your Option ")
        ch = input("Enter your choice : ")


        if ch == '1':
        #customer portal
            print("\t1. ARE YOU AN EXISTING CUSTOMER? (Y/N) ")
            choice = input("Enter your choice : ")
            if (choice == 'Y' or choice == 'y'):
                cusid = int(input("\t Enter your customer id: "))
                found_customer = bank.find_customer(cusid)
                if found_customer == None:
                    print("\tINVALID CUSTOMER ID")
                    break

            elif (choice == 'N' or choice == 'n'):
                
                name = input("Enter the account holder name : ")
                address = input ("Enter mailing address : ")
                found_customer = bank.create_customer(name, address)
            else:
                print("\tINVALID CHOICE")
                break

            customerPortal(bank,found_customer)


                       
        elif ch == '2':
        #employee portal   
            employeePortal(bank)

        elif ch=='3':
            print("\tThank you for using the banking system. Have a nice day!")
            break

        else:
            print("Invalid choice")

    bank.close_bank()

