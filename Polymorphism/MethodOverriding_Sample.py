
#   METHOD OVERRIDING IS ALSO KNOWN AS RUN TIME POLYMORPHISM

class Employee:
    def calculate_salary(self):
        return 0

class FullTimeEmployee(Employee):

    def calculate_salary(self):
        return 90000

class PartTimeEmployee(Employee):

    def calculate_salary(self):
        return 30000

def get_employee_salary(emp):
    return emp.calculate_salary()

emp1 = FullTimeEmployee()
emp2 = PartTimeEmployee()

print(get_employee_salary(emp1))