chest_exercies = ["Bench Press", "Pec Dec Flies", "Inclined Doumbelle press", "High to Low cable flies", "Machine Press", "Inclined Bench Press", "Declined Bench Press", "Declined Doumbelle Press"]

while True:
    selection_mode = input("Type name or index for selecting a exersie selection mode ")
    if (selection_mode =="name" or selection_mode =="index"):                              
        break
    print("Please type in a correct selection mode input.")

def exercise_datainput(exercise_index):
    print(f"U have selected {chest_exercies[exercise_index]} exersice")
    exercise_set_1 = input("Enter the weight, reps in 1 set")
    exercise_set_2 = input("Enter the weight, reps in 2 set")
    exercise_set_3 = input("Enter the weight, reps in 3 set")
    
    exercise_data = [exercise_set_1, exercise_set_2, exercise_set_3]
    print(exercise_data)


if (selection_mode =="name"):
    exercise_name = (input("Enter the name of chest exersise u want to make entry of "))
    exercise_index = chest_exercies.index(exercise_name)
    exercise_datainput(exercise_index)

elif(selection_mode == "index"):
    exercise_index = int(input("Enter the index of chest exersise u want to make entry of "))
    exercise_datainput(exercise_index)


