marks = {"Arsh": 27, "Anvesh": 13, "Gitansh": 29.5, "Manasvi": 30, "Divyanka": 29.5}

print(marks, "type", type(marks))
print(marks["Anvesh"], "type", type(marks))

marks["Anvesh"] = 28  #muteable
print(marks["Anvesh"])

marks["Ritul"] = 17  # adding new data in dictuniary
print(marks)

while True:
    studentName = input("Enter the name of the student you want to know the marks of: ")
    
    if studentName in marks:
        print(f"{studentName}'s marks: {marks[studentName]}")
    else:
        print(f"Name \"{studentName}\" not found")

