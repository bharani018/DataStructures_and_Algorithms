
#HIERARCHIAL INHERITANCE IS THE PROCESS IN WHICH SINGLE BASE CLASS IS INHERITED TO TWO OR MORE DERIVED CLASS

class Number:

    def __init__(self, a, b):
        self.a = a
        self.b = b

class Sum(Number):
    def sumOfNumbers(self):
        return self.a + self.b

class Product(Number):
    def productOfNumbers(self):
        return self.a * self.b

add = Sum(2,3)
print(add.sumOfNumbers())

mult = Product(2,3)
print(mult.productOfNumbers())
