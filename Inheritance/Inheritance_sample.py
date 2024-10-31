
#INHERITANCE: IT IS THE PROCESS OF INHERITING THE PROPERTIES OF PARENT CLASS TO THE CHILD CLASS

class Parent_class:

    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def area(self):
        return self.a*self.b

class Child_class(Parent_class):
    def SquareAndProduct(self):
        return (self.a*self.a)*(self.b*self.b)


obj = Child_class(2,3)
print(obj.a)    #Accessing parent class variable 
print(obj.area())   #Accessing parent class method
print(obj.SquareAndProduct())   #Accessing child class Method with parent class variables