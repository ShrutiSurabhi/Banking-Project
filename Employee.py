import Person as Person
class Employee(Person.Person):
    def __init__(self, index, name, address): 
        self.index = index
        super().__init__(name, address)
    
