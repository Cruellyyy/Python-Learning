lists = [1, 99, 98, 3, 6]

def square(x):
    return x*x

newlist = list(map(square, lists))
print(newlist)