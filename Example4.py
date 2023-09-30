#Hierarchical Inheritance
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Employee(person):
    def __init__(self,id,salary):
        super().__init__("hari",20)
        self.employee_id=id
        self.salary=salary
    def disp(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("EMPLOYEE ID:",self.employee_id)
        print("Salary:",self.salary)

class student(person):
    def __init__(self,id1,gpa):
        super().__init__("kishore",19)
        self.std_id=id1
        self.gpa=gpa
    def disp(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("STUDENT ID:",self.std_id)
        print("GPA:",self.gpa)  

ob1=student("18","8.6")
ob2=Employee("22",12000)
ob2.disp()
ob1.disp()                             
