while True:
    try:
        a = int(input("Enter the 1st number: "))
        b = int(input("Enter the 2st number: "))
        if b == 0 or a == 0:
            raise ValueError("Please dont using zeros while suming")
        c = int(input("Enter the 3st number: "))    


        print(f"The sum of abc is: {(a+b)/c}")
        
    except ZeroDivisionError as e:
        print(f"The number can not be divible by zero {e}")
    except ValueError as e:
        print(f"Please only enter integer value. {e}")
    except Exception as e:
        print(e)
    else:
        print("No errors")
    finally:
        print("This runs every time")

