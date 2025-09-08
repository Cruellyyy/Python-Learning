class Vehicle:
    def __init__(self, capacity):
        self.capacity = capacity
    def drive(self):
        print("Driving the vehicle.")

class Car(Vehicle):
    def drive(self):
        print("Driving a car, playing music...")

class Bus(Vehicle):
    def drive(self):
        print("Bus driving, announcing next stop...")

class Bike(Vehicle):
    def drive(self):
        print("Bike zooming on the road!")

vehicleList = [Vehicle(90),
               Car(4),
               Bus(20),
               Bike(3),
               Car(9)]

def startRoute():
    for V in vehicleList:
        V.drive()

startRoute()