#Encapsulation
class fun:
    def __init__(self):
        self.a=10      #public 
        self._b=20     #protected 
        self.__c=30    #private

    def disp(self):
        print("C:",self.__c)    

class cal(fun):
    def display(self):
        print("A:",self.a)
        print("B:",self._b)

ob1=cal()
ob1.display()
ob1.disp()        
