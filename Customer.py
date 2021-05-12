import Person as Person
class Customer(Person.Person):
    
    #deposit = 0

    def __init__(self, index, name, address, customer_id, account_nos):     
        super().__init__(name, address)  
        self.customer_id = int(customer_id)
        self.account = str(account_nos).split('^')
        self.index = index

    def __eq__(self, other):
        if isinstance(other,Customer):
            return self.customer_id == other.customer_id
        else:
            return self.customer_id == other
        
        
    def create_account(self, acc_obj):
        
        self.account.append(acc_obj.account_no)
        print(f"\n\nAccount Created forasdasda {self.name}\n** Details as follows **\nAccount number: {acc_obj.account_no}\nType of account: {acc_obj.acc_type} \nMailing address: {self.address}\n Initial Deposit: {acc_obj.total_amt}")
       
            
            
    def show_accounts_info(list_customers):
        
        unpack_list = [*enumerate(list_customers)]
        print(unpack_list)

    def as_dict(self):
        
        if (len(self.account) == 0):
            acc = ""
        else:
            acc = "^".join(self.account)
        return {"Name" : self.name, "Address" : self.address,"Customer id" : self.customer_id,"Account Number(s)" : acc}
        
       
            
        #with open('innovators.csv', 'r') as file:
        #reader = csv.reader(file)
        #for row in reader:
        #print(row)
