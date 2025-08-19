a = {92,99,11,34,93}
b = {23,93,92,25,99}
c= a.union(b)  #contains all the unique elemets from a and b
print(c)

print(a.intersection(b)) #d contian only the elements which both a and b contains

print(a.difference(b))