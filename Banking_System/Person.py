import pandas as pd
import os

class Person():
    
    name = ''
    address = ''
    
    def __init__(self, name, address):
        self.name = name
        self.address = address
