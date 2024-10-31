#    METHOD OVERLOADING IS ALSO KNOWN AS COMPILE TIME POLYMORPHISM

class Calculator:

    
    def Addition(self, num1 = 0, num2 = 0, num3 = 0):
        return num1+num2+num3

    def Subtraction(self, num1 = 0, num2 = 0, num3 = 0):
        return num1 - num2 - num3

obj = Calculator()
print(obj.Addition(3, 4))
print(obj.Subtraction(3,num3=4))

#OPERATOR OVERLOADING

class TryOperatorOverloading:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, others):
        return TryOperatorOverloading(self.x + others.x , self.y + others.y)

    
    def __str__(self):
        return f'{self.x}, {self.y}'


point1 = (TryOperatorOverloading(2, 4))
point2 = TryOperatorOverloading(3, 1)
point3 = point1 + point2
print(point3)