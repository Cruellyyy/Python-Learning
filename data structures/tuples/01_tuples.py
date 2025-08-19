tuples= (1120, "ijhfwijnf", 24.24, True) #same as list, but immuteable and assigned by ()

print(tuples)
print(tuples[1])

'''
tuples[2] = 923  not work as immutebale
tuples.append    not even supports this function
'''

# so unlike lists, u cannt create a tuple with one elemets like this-
lists= [1]  #it will considered as list
tuple_2 = (2) #not considered as tuples
real_one_tuple = (2,)  #u need to add a comma to make a one value tuples
