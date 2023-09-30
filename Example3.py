# single inheritance
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class student(person):
    section="A"
    def display(self):
        print("NAME:",self.name)
        print("AGE:",self.age)
        print("SECTION:",self.section)

std1=student("jagan",18)

std2=student("adi",18)

std1.display()
std2.display()
