
class PrivateMethod:
    def __init__(self, a, b=0):
        self.a = a
        self.__b = b

    def _CreateMethodForProtected(self):
        return f'Protected method, value {self.a}'

    def __CreateMethodForPrivate(self):
        return f'Private method, value {self.a}'

    def Sample(self):
        newVariable = self.__CreateMethodForPrivate()
        return f'Accessing private method using getter method {newVariable}'
    
class ChildClass(PrivateMethod):
    def NewMethod(self):
        return f'Inherited class, value {self.a}'

obj = ChildClass(3)
print(obj._CreateMethodForProtected())
print(obj.NewMethod())
print(obj.Sample())

#To access the Private Method we should create a new instance for Parent class
obj2 = PrivateMethod(1)

print(obj2._PrivateMethod__b)

