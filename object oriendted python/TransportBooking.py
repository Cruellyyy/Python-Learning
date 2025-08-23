class vehicle:
    def __init__(self, vehicleType, modelNo, totalSeats,):
        self.vehicleType = vehicleType
        self.modelNo = modelNo
        self.totalSeats = totalSeats
        self.bookedSeats = []
        self.bookedSeatsDictNames = {}

    def showAvailableSeats(self):
        self.available = [seat for seat in range(1, self.totalSeats+1) if seat not in self.bookedSeats]
        print(f"The following seats are available {self.available}")
    def bookingSeat(self, value, name):
        if(value <= self.totalSeats and value not in self.bookedSeats):
            self.bookedSeats.append(value)
            self.bookedSeatsDictNames[value] = name
            print(f"UR seat no. {value} has been booked by name \"{name}\"")
        elif(value <= self.totalSeats and value in self.bookedSeats):
            print(f"The seat no {value} is not available at the moment ")
    def cancelBooking(self, value):
        if(value in self.bookedSeats):
            name = input("Enter the name by which u had booked the seat ").lower().strip()
            if value in self.bookedSeats and self.bookedSeatsDictNames[value] == name:
                 self.bookedSeats.remove(value)
                 del self.bookedSeatsDictNames[value]
                 print(f"The booked seat \"{value}\" has been canceled by \"{name}\"")
            else:
                print("The booked seat u are trying to cancel is was not booked by this name, u can not cancel a booked seat of another person.")
        else:
            print("How can I cancel booking of a seat which is not booked yet?")
    def showBookedSeats(self):
        print("This is the list of booked seats ", self.bookedSeats)

vehicles = [vehicle("Bus", 920938, 50),
            vehicle("Aeroplane", 234342, 150),
            vehicle("Train", 234234, 200),
            vehicle("boat", 234234, 7),
            vehicle("yart", 234234, 93),
            ]

print("Welcome to the vehicle booking system")

while True:
    inputValue = input("Enter the name of the vehicle ")
    for vehicle in vehicles:
      if vehicle.vehicleType.lower() == inputValue.lower():
         print("\nEnter 1 to show available seats  \n2 to book a seat \nand 3 to cancel a booked seat.\n")
         method = int(input())
         if method == 1:
             vehicle.showAvailableSeats()
         if method == 2: 
            vehicle.showAvailableSeats()
            value = int(input("Enter the seat u wanna book "))
            name = input("Enter ur name for boooking the seat ").strip().lower()
            vehicle.bookingSeat(value, name)
         if method == 3:
             vehicle.showBookedSeats()
             value = int(input("Enter the seat u wanna cancel booking of "))          
             vehicle.cancelBooking(value)
