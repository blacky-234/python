from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
   
   def move(self):
        print("Car is moving")

c = Car()  # ❌ Error: Can't instantiate abstract class Car without start()
c.move()