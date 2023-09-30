# calculating perosn age
class person:
    def __init__(self,name,country,dob,year):
        self.name=name
        self.counrty=country
        self.yearofbirth=dob
        self.currentyear=year

    def age(self):
        return self.currentyear - self.yearofbirth
    def display(self):
        print("NAME:",self.name)
        print("COUNTRY:",self.counrty)
        print("BORN IN:",self.yearofbirth)
        print("CURRENT AGE:",self.age())

ob1=person("Jagan","India",2005,2023)
ob1.display()        
