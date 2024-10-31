#Operator overloading
class point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, others):
        return point(self.x + others.x , self.y + others.y)

    def __str__(self):
        return f"point: {self.x, self.y}"


p1 = point(2,3)
p2 = point(4,5)

result = p1+p2
print(result)



#Overloading

class ArithmeticOperation:
    def add(self, a=0, b=0, c=0):
        return a+b+c 
    
su = ArithmeticOperation()
print(su.add(1,2)) 
print(ArithmeticOperation.a)
