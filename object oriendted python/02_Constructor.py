class Bike:
    company = "motorola"
    def __init__(self, company, model, price, topSpeed):
        self.company = company
        self.model = model
        self.price = price
        self.topSpeed = topSpeed
    def getBikeDetails(self):
        print(f"Company = {self.company}")
        print(f"Model = {self.model}")
        print(f"Price = {self.price}")
        print(f"Top speed = {self.topSpeed}")

bike1 = Bike("Kawasaki", "Z900", 1079000, "250 km/h")
bike2 = Bike("Ducati", "Panigale V4", 2499000, "299 km/h")
bike3 = Bike("BMW", "S1000RR", 1899000, "305 km/h")
bike4 = Bike("KTM", "Duke 390", 450000, "170 km/h")
bike5 = Bike("Yamaha", "R15 V4", 180000, "180 km/h")
bike6 = Bike("Honda", "CBR650R", 900000, "220 km/h")

print(bike1.company)  #this will print instance attribute if present
print(Bike.company)  #this will always print class attibute
print(dir(bike1))

while True:
        inputBike = input("Enter the bike variable name to get all the details ")
        if inputBike == "bike1":
         bike1.getBikeDetails()
        elif inputBike == "bike2":
            bike2.getBikeDetails()
        elif inputBike == "bike3":
            bike3.getBikeDetails()
        elif inputBike == "bike4":
            bike4.getBikeDetails()
        elif inputBike == "bike5":
            bike5.getBikeDetails()
        elif inputBike == "bike6":
            bike6.getBikeDetails()
        else: print(f"there is no variable named {inputBike}")
        
