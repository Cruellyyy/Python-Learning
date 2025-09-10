from functools import reduce

list1 = [1, 2, 3, 4, 5, 6]

newList = reduce(lambda a , b: (a+b), list1 )
print(newList)