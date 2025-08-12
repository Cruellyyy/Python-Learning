name = "Arsh Khan" #strings are immuteable, u may assign the var different string but it still exsit in memory
print(name.upper(), name)
print(name.lower(), name) #here name prints the original string and .lower and .upper create different version of it instead of modifing the original var value
print(name.capitalize())
print(name.title())

# name[0] = "H"  # not gonna work, shows an error

nameLenght = len(name)
print(nameLenght)

text = "  arsh  khan  "
print(text.strip())  #remove spaces from both right and left side
print(text.rstrip())  #remove spaces from right side only
print(text.lstrip())  #remove spaces from left side only

print(text.find("khan"))  #give index of frist set character 
print(text.strip().replace("arsh", "harsh"))

list_txt = "apple , banana , berry"
print(list_txt.split(","))
print(",".join ( ['apple ', ' banana ', ' berry']))

print(text.isalnum())
print(text.isdigit())
print(text.isalpha())
print(text.islower())
