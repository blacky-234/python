class Animal:

    def speak(self):
        print("Animal Speaking")

class Dog(Animal):

    def speak(self):
        print("Dog Barking")

class Cat(Animal):
    pass

d = Dog()
d.speak()
c = Cat()
c.speak()