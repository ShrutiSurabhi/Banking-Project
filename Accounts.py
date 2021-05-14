import pandas as pd
import os
import random
import csv
import collections

class Accounts:
    
    option = 0

    def __init__(self, index, customer_id, account_no, acc_type, total_amt):
        
        self.index = index
        self.customer_id = customer_id
        self.account_no = account_no
        self.acc_type = acc_type
        self.total_amt = total_amt
        
    def __eq__(self, other):

        if isinstance(other,Accounts):
            return self.account_no == other.account_no
        else:
            return self.account_no == other

    def depositAndWithdraw(self, currency, option):

        if option == 1:
            self.total_amt = self.total_amt + currency

        elif option == 2:

            if (self.total_amt >= currency):
                self.total_amt = self.total_amt - currency
            else:
                print("Insufficient balance :(")

    def displayBalance(self, accNo):
        print("f\tThe balance for {self.account_no} is : {self.total_amt} \n")

    def show_account_info(self):
        print(f"Account Number : {self.account_no}\n Type : {self.acc_type}\n Total Amount : {self.total_amt}\n\n")

    def as_dict(self):
        return {"Customer id" : self.customer_id,"Account Number" : self.account_no, "Type" : self.acc_type, "Total Amount" : self.total_amt}
      