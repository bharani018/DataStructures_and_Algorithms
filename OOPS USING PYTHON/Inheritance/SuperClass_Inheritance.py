#SUPER CLASS: super() function IS USED TO CALL THE METHOD DEFINED IN THE PARENT CLASS AND ENABLES IT EXTEND OR CUSTOMIZE IT IN CHILD CLASS

class Employee:
    def __init__(self, name, id, age):
        self.name = name
        self.id = id
        self.age = age
    
class Details(Employee):
    def __init__(self, name, id, age, Email, address):
        super().__init__(name, id, age)
        self.Email = Email
        self.address = address
    
    def display(self):
        return f'{self.name} -  {self.age}  -  {self.id} - {self.Email}  -  {self.address}'

obj2 = Details('ABC', 123, 23, 'abc@gmail.com', 'CHENNAI')

print(obj2.display())