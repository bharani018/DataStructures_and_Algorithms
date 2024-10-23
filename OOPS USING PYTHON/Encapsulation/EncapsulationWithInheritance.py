
''' Create a base class Person with:

Private attribute __name and protected attribute _age.
Public methods to set and get both name and age.
Create a derived class Student that inherits from Person and:

Adds a private attribute __grade.
Adds methods to set and get the __grade. '''

class Person:

    def __init__(self, name, age):
        self.__name = name
        self._age = age

    def setName(self, newName):
        self.__name = newName
    
    def getName(self):
        return self.__name

    def setAge(self, newAge):
        self._age = newAge

    def getAge(self):
        return self._age

class Student(Person):

    def __init__(self, grade, name, age):
        super().__init__(name, age)
        self.__grade = grade

    def setGrade(self, Newgrade):
        self.__grade = Newgrade

    def getGrade(self):
        return  self.__grade

    def GetFullDetails(self):
        return f'Name:{self.getName()}, age: {self.getAge()}, Grade: {self.getGrade()}'

stud1 = Student('A', 'Bharani', 20)

stud1.setName('Bharani Kumar ')
stud1.setAge(21)

print(stud1.getAge())
print(stud1.getName())
print(stud1.GetFullDetails())


    