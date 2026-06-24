class Vehicle:
    def __init__(self,name):
        self.name = name

    def start(self):
        print(f"{self.name} Vehicle has started....")

class Car(Vehicle):
    def start(self):
        print(f"{self.name} Car has started")

class Bike(Vehicle):
    def start(self):
        print(f"{self.name} Bike has started")

class Truck(Vehicle):
    def start(self):
        print(f"{self.name} Truck has started")

car1 = Car("Mercedes")
bike1 = Bike("BMW")
truck1 = Truck("Lamborghini")

car1.start()
bike1.start()
truck1.start()