class Vehicle:

    def __init__(self, brand):
        
        self.brand = brand
    
    def info(self):
        
        print(f"Brand: {self.brand}")

class Car(Vehicle):

    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
    
    def info(self):
        super().info()
        print(f"Model: {self.model}")



car = Car("Toyota", "Camry")
car.info()
    