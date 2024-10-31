#HYBRID INHERITANCE : IT IS THE COMBINATION OF MORE THAN ONE TYPE OF INHERITANCE (IT MIGHT BE MULTIPLE, MULTILEVEL ...)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        return f'{self.name} - {self.age} '

class Student(Person):  #HERE STUDENT CLASS IS DERIVED FROM PERSON CLASS --- SINGLE INHERITANCE
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self):
        return f'{self.name} is studying...'

class Teacher(Person):  #HERE TEACHER CLASS IS DERIVED FROM PERSON CLASS ---- HIERARCHIAL INHERITANCE
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def teach(self):
        return f'{self.name} teaches {self.subject}'

class ResearchScholar(Student, Teacher):  #HERE RESEARCH SCHOLAR CLASS IS DERIVED FROM BOTH STUDENT AND TEACHER CLASS  ---- MULTIPLE INHERITANCE
    def __init__(self, name, age, student_id, subject):
        Person.__init__(self, name, age)
        self.student_id = student_id
        self.subject = subject
    
    def display(self):
        return f'{self.name} teaches {self.subject} and student id {self.student_id}'


res = ResearchScholar(23, 23,23,23)
print(res.display())


# SO COMBINATION OF SINGLE INHERITANCE MULTIPLE INHERITANCE HIERARCHIAL INHERITANCE IS CALLED HYBRID INHERITANCE
