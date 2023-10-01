#polymorphism
class Employee:
    def __init__(self,name,sal):
        self.employee_name=name
        self.employee_salary=sal

class Managar(Employee):
    deparment=""
    def __init__(self,name,sal):
        super().__init__(name,sal)
    def display(self):
        print("EMPLOYEE NAME:",self.employee_name)
        print("EMPLOYEE SALARY:",self.employee_salary)
        print("DEPARTMENT:",self.department)

    @classmethod  
    def age(cls,age):
        cls.age=age
        print("AGE:",cls.age)    



object=Managar(input(),int(input()))
Managar.department="IT"               
object.display()
Managar.age(18)
