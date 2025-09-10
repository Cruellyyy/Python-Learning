from functools import reduce
def sum(*args):
    print(args)
    total = ()
    return reduce(lambda a, b : a+b, args)

lists = [878, 989, 5468, 869]
print(a:= sum(223, 92, 10, 0))

#for list, can do something like this
def sumLists(lists):
    print(lists)
    total = ()
    return reduce(lambda a, b : a+b, lists)

lists = [878, 989, 5468, 869]
print(b:= sumLists(lists))

