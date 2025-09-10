def checkIfNumLessthan69(x):
    if x < 69:
        return True
    else: return False

lists = [9, 90, 376, 20, 38, 49, 9273,873, 28]
newlist = tuple(filter(checkIfNumLessthan69, lists))
print(newlist)