import Person as Person

class Customer(Person.Person):
    
    def __init__(self, index, name, address, customer_id, account_nos):     
        super().__init__(name, address)
        self.customer_id = int(customer_id)
        self.account = str(account_nos).split('^')
        self.index = index

    def __eq__(self, other):
        if isinstance(other,Customer):
            return self.customer_id == other.customer_id
        else:
            return str(self.customer_id) == str(other)
        
        
    def create_account(self, acc_obj):

        if(self.account[0] == ''):
            self.account[0]  = acc_obj.account_no
        else:
            self.account.append(acc_obj.account_no)
        print(f"\n\nAccount Created for {self.name}\n** Details as follows **\nAccount number: {acc_obj.account_no}\nCustomer_id: {acc_obj.customer_id}\nType of account: {acc_obj.acc_type} \nMailing address: {self.address}\n Initial Deposit: {acc_obj.total_amt}\n")

    def get_account_id(self):
        
        if (len(self.account) == 0):
            print("\tYou don't have an active account")
            return None
        
        
        for index, acc in enumerate(self.account):
            print(f"\t {index+1} : {acc}")
        ch = int(input("\nSelect the account you want to proceed with: "))
        if (ch > len(self.account)):
            print("\n\tInvalid choice")
            return None
        return self.account[ch-1]


    def deleteAccount(self, acc_no):

        self.account.remove(acc_no)
        print("\n Account deleted! \n")

    def modifyCustomerInfo(self):

        while (ch != 3):

            print("CHOOSE INFO TO BE MODIFIED \n")
            print("1. NAME ")
            print("2. MAILING ADDRESS")
            print("3. EXIT")

            ch = int(input("Please choose one to procede"))
            print("\n")
            if (ch == 1):
                new_name = input("ENTER THE NEW NAME: ")
                self.name = new_name
                print("THE INFO MODIFIED SUCCESSFULLY\n")
            elif(ch == 2):
                new_address = input("ENTER THE NEW MAILING ADDRESS: ")
                self.address = new_address
                print("THE INFO MODIFIED SUCCESSFULLY\n")
                


            
    def show_customer_info(self):
        print(f"Name:  {self.name}\n Address: {self.address}\n Customer id: {self.customer_id}\n Account Number(s) : {self.account}\n\n")

    def as_dict(self):
        
        if (len(self.account) == 0):
            acc = ""
        else:
            acc = "^".join(self.account)
        return {"Name" : self.name, "Address" : self.address,"Customer id" : self.customer_id,"Account Number(s)" : acc}
        
    