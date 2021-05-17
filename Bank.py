import pandas as pd
import os
import random
import csv
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
    ACC_SIZE=10
    
    def __init__(self, customer_file, account_file):
        
        self.customer_file = customer_file
        self.account_file = account_file
       
     
    def read_data(self):
        
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
            acc = Accounts(index, row["Customer id"],row["Account Number"], row["Type"], row["Total Amount"])
            self.list_accounts.append(acc)
        
        #-----------------------------------------------------------
        

    def find_customer(self,customer_id):
        if customer_id in self.list_customers:
            return self.list_customers[self.list_customers.index(customer_id)]
        return None

    def find_account(self,account_no):
        if account_no in self.list_accounts:
            return self.list_accounts[self.list_accounts.index(account_no)]
        return None


    def create_customer(self, name, address):

        cusid = self.get_unique(2)
        cid = Customer(len(self.list_customers), name, address, cusid, "")
        self.list_customers.append(cid)
        
        return cid 

    def create_account(self, acc_type, deposit, found_customers):

        acc_id = str(self.get_unique(1))
        acc_obj = Accounts(len(self.list_accounts), found_customers.customer_id, acc_id, acc_type, deposit)
        self.list_accounts.append(acc_obj)
        
        return acc_obj 

    def get_unique(self,option):
        if (option == 1):
            acc_no = random.randint(10**self.ACC_SIZE, (10**(self.ACC_SIZE+1))-1)
            while acc_no in self.list_accounts:
                acc_no = random.randint(10**self.ACC_SIZE, ((10**self.ACC_SIZE+1))-1)
            return acc_no
        if (option == 2):
            cusid = random.randint(100000, 900000)
            while cusid in self.list_customers:
                cusid = random.randint(100000, 900000)
            return cusid


    def close_bank(self):
    #to close csv files and so saving all the content in dataframe to csv files
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
        choice = input("\tSelect Your Option (1-7) ")
        print("\n")

        if choice == '1':
            #interaction for creating an account        
            
            acc_type = input("Enter the type of account [Current/Saving] : ")
            deposit = int(input("Enter the initial amount ($) []>=500 for Saving and >=1000 for current] : "))
            acc_obj = bank.create_account(acc_type, deposit, found_customer)
            found_customer.create_account(acc_obj)

        elif choice =='2':
         
            acc_no = found_customer.get_account_id()
            found_account = bank.find_account(acc_no)
            currency = int(input("\t\nEnter the amount you want to deposit ($) : "))
            found_account.depositAndWithdraw(currency, 1)
            print("Transaction successful!\n\n")

        elif choice == '3':

            acc_no = found_customer.get_account_id()
            found_account = bank.find_account(acc_no)
            currency = int(input("\t\nEnter the amount you want to withdraw ($) : "))
            found_account.depositAndWithdraw(currency, 2)
            print("Transaction successful!\n\n")

        elif choice == '4':
        #displays specific account number's balance
            acc_no = found_customer.get_account_id()
            found_account = bank.find_account(acc_no)
            found_account.displayBalance()

        elif choice == '5':
        #deletes account    
            acc_no = found_customer.get_account_id()
            found_account = bank.find_account(acc_no)
            bank.list_accounts.remove(found_account)
            found_customer.deleteAccount(acc_no)
            

        elif choice == '6':
        #modifies customer's info
            found_customer.modifyCustomerInfo()

        elif choice == '7':
            print("\tThank you for using bank managemnt system. Have a nice day!\n\n")
            break

        else:
            print("Invalid choice\n")
        input("Press enter to continue")

def employeePortal(bank):

    choice = ''
    num = 0
    while choice != 4:

        print("\tCHOOSE ONE TO PROCEDE")
        print("\t1. CUSTOMERS NAME AND THEIR INFORMATION")
        print("\t2. ACCOUNTS LIST AND THEIR INFORMATION")
        print("\t3. TOTAL CLOSING DAY BANK BALANCE ")
        print("\t4. EXIT")
        
        ch = input("\t\nSelect Your Option (1-4): ")
        print("\n")

        if ch == '1':
        #
            for row in bank.list_customers:
                row.show_customer_info()
            

        elif ch =='2':

            for row in bank.list_accounts:
                row.show_account_info()

        elif ch == '3':
            total_amount = 0
            for row in bank.list_accounts:
                total_amount = total_amount + row.total_amt
            print (f"TOTAL CLOSING DAY BANK BALANCE: ${total_amount}")


        elif ch == '4':
            print("\tThank you for using the banking system. Have a nice day!")
            break
        else:
            print("Invalid choice")
        input("Press enter to continue\n\n")
            

    



if __name__ == "__main__":    
#start of the program

    
    #bank = Bank("C:\\Users\\shrut\\OneDrive\\Desktop\\Banking\\employee_data.csv","C:\\Users\\shrut\\OneDrive\\Desktop\\Banking\\customer_data.csv" , "C:\\Users\\shrut\\OneDrive\\Desktop\\Banking\\account_data.csv" )
    bank = Bank("customer_data.csv" , "account_data.csv" )
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
        
        ch = input("\tSelect Your Option (1-3) : ")
        print("\n")


        if ch == '1':
        #customer portal
            print("\t1. ARE YOU AN EXISTING CUSTOMER? (Y/N) ")
            choice = input("Select Your Option : ")
            if (choice == 'Y' or choice == 'y'):
            #if the customer is existing, enter the customer id to proceed
                cusid = int(input("\t Enter your customer id: "))
                found_customer = bank.find_customer(cusid)
                #'find_customer' searches the customer. when found, object created 'found_customer' with all info

                if found_customer == None:
                    print("\tINVALID CUSTOMER ID")
                    break

            elif (choice == 'N' or choice == 'n'):
            #if the customer is new, enter the name and address to proceed    

                name = input("Enter the account holder name : ")
                address = input ("Enter mailing address : ")
                found_customer = bank.create_customer(name, address)
                #'create_customer' creates the customer. Object created 'found_customer' with all info
            else:
                print("\tINVALID CHOICE")
                break

            customerPortal(bank,found_customer)
            #in both conditions 'customerportal' is called with the bank(object of class Bank) and found_customer(obejct of a particular customer) as parameters

                       
        elif ch == '2':
        #employee portal   
            employeePortal(bank)

        elif ch=='3':
            print("\tThank you for using the banking system. Have a nice day!\n\n")
            break

        else:
            print("Invalid choice")

    bank.close_bank()
    #to close and save the content in csv files
