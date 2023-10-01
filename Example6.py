#polymorphism
class shape:
    def Area(self):
        return 0
    
class rectangle(shape):
    def __init__(self,len,breadth):
        self.length=len
        self.breadth=breadth
    def Area(self):
        return self.length *self.breadth
    
object=rectangle(int(input()),int(input()))
print("Area of rectangle:",object.Area())    
    