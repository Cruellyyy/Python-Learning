userPassList = {"arsh":"khan"}
class user:
    def __init__(self, username, password, ):
        self.username = username
        self.password = password
    def create_acc(self):
        global userPassList
        if(self.username in userPassList):
            print(f"An account already exist with username\"{self.username}\", please proceede with a different username.")
        elif(self.username not in userPassList):
            userPassList[self.username] = self.password
            print(f"Ur account has been successfully created,\nusername :- \"{self.username}\" \npassword :- \"{self.password}\"")
    def login(self):
        global userPassList
        if (userPassList[self.username] == self.password):
            return self.username
        elif(self.username in userPassList):
            print(f"Invalid password for username {self.username}")
            return None
        else: 
            print(f"The acc with the username \"{self.username}\" does not exsits.")
            return None

class vehicle:
    def __init__(self, vehicleType, modelNo, totalSeats, ):
        self.vehicleType = vehicleType
        self.modelNo = modelNo
        self.totalSeats = totalSeats
        self.bookedSeats = []
        self.bookedSeatsDictNames = {}

    def showAvailableSeats(self):
        self.available = [seat for seat in range(1, self.totalSeats+1) if seat not in self.bookedSeats]
        print(f"The following seats are available {self.available}")
    def bookingSeat(self, username, value):
        if(value <= self.totalSeats and value not in self.bookedSeats):
            self.bookedSeats.append(value)
            self.bookedSeatsDictNames[value] = username
            print(f"UR seat no. {value} has been booked by name \"{username}\"")
        elif(value <= self.totalSeats and value in self.bookedSeats):
            print(f"The seat no {value} is not available at the moment ")
    def cancelBooking(self, username, value):
        if(value in self.bookedSeats):
            if value in self.bookedSeats and self.bookedSeatsDictNames[value] == username:
                 self.bookedSeats.remove(value)
                 del self.bookedSeatsDictNames[value]
                 print(f"The booked seat \"{value}\" has been canceled by \"{username}\"")
            else:
                print("The booked seat u are trying to cancel is was not booked by account, u can not cancel a booked seat of another person.")
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
    print("1. Create account \n2. Login")
    userClassInput = int(input(""))
    if(userClassInput == 1):
        username = input("Enter a username to create an acc ")
        password = input("Enter a password for it ")
        newUser = user(username, password)
        newUser.create_acc()
    elif(userClassInput == 2):
        username = input("Enter ur username ")
        password = input("Enter ur password ")  
        login_user = user(username, password)
        vehicleUser = login_user.login()   
        
        inputValue = input("Enter the name of the vehicle: ").lower()
        selected_vehicle = None

        # Find the matching vehicle
        for v in vehicles:
            if v.vehicleType.lower() == inputValue:
                selected_vehicle = v
                break

        if selected_vehicle:
            while True:
                print("\n1. Show available seats")
                print("2. Book a seat")
                print("3. Cancel a booking")
                print("4. logout")
                
                try:
                    method = int(input("Enter your choice (1-4): "))
                    
                    if method == 1:
                        selected_vehicle.showAvailableSeats()
                    elif method == 2:
                        selected_vehicle.showAvailableSeats()
                        value = int(input("Enter the seat number you want to book: "))
                        selected_vehicle.bookingSeat(vehicleUser, value)
                    elif method == 3:
                        selected_vehicle.showBookedSeats()
                        value = int(input("Enter the seat number to cancel: "))
                        selected_vehicle.cancelBooking(vehicleUser, value)
                    elif method == 4:
                        break
                    else:
                        print("Invalid choice! Please select 1-4")
                except ValueError:
                    print("Please enter a valid number")
        else:
            print(f"No vehicle found with name '{inputValue}'")

