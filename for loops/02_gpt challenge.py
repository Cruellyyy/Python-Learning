ValueOf_N = int(input("Please enter the n value"))

FizzBuzz = 0
Fizz = 0
Buzz = 0

for i in range(1,ValueOf_N + 1): 
      
      if (i % 5 == 0 ) and (i % 3 == 0):
         print("FizzBuzz")
         FizzBuzz += 1
      elif (i % 5 == 0):
        print("Buzz")
        Buzz += 1
      elif (i % 3 == 0):
        print("Fizz")
        Fizz += 1
      else:
        print(i)

print ("FizzBuz = " ,FizzBuzz)

print ("Fizz = " ,Fizz)

print ("Buzz = " ,Buzz)

