# import random
# correctNumber = random.randint(1, 100)

# userGuess = None
# guess_counts = 0

# while userGuess != correctNumber:
#     userGuess = int(input("Guess the number between 1 to 100 :- "))
#     guess_counts += 1
#     print("Sorry, u guessed the number incorrectly" , "(" ,userGuess ,")" )
#     print ("Please try again")

# print("U guessed the number correctly :-", correctNumber,)
# print("number of guesses :-" , guess_counts )

import random

print("Can u guess me, I am a number between 1 to 10!")

correct_num = random.randint(1, 10)
guess_counts = 0

while True:
    user_guess = int(input("Enter ur guess number :- "))

    if user_guess == correct_num:
        print ("U have guessed the number correctly " , "(" , correct_num, ")")
        break
    else:
        print("U have guessed the number incorrectly" , "(" , user_guess, ")" )
        guess_counts += 1



