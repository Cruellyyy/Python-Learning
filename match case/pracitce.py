chossedLuckyNumber = int(input("Enter a number form 1 to 10 :- "))

match chossedLuckyNumber:
    case 4: 
        print("u just won a car")
    
    case 9:
        print("u just won a bike")
    
    case 6: 
        print("u just won a gf")
    
    case _:
        print("Sorry, better luck next time")