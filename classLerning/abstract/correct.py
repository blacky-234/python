from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
   
   def start(self):
       print("Car is starting")
   
   def move(self):
        print("Car is moving")

c = Car() 
c.move()
c.start()