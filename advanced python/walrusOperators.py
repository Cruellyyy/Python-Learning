def printing_something(n =6):
    for i in range(1, n + 1):
        print("Something is printed")
    return n

if printing_something() > 5:
    print(printing_something())  #so here it is calling the function again to get the retrun value

#fixing
a = printing_something()  #we can solve this by storing the function and its return value into an varibale
if a > 5:
    print(a)  #after the function runs, value of a become the return function, so we can print it without calling the func again

#but there is a better way to do this using walrus operator (:=)
if (b:= printing_something()) > 4:
    print(b)

while (data := input("ENter the value: ")):
    print(data)
    if data == "q":
        print("Quiting")
        break