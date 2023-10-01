#Multiple Inheritace
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog:
    def sound(self):
        super().sound()
        print("Dog barks")

class Bird(Dog,Animal):
    def sound(self):
        super().sound()
        print("Bird sings")

object=Bird()
object.sound()                        