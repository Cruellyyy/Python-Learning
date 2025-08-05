a = 31
b = "3"

print (type(a))  # This will print <class 'int'>
print (type(b))  # This will print <class 'str'>    

# print(a + b)   not working because a is int and b is str
# Type casting b to int
c =  int(b)  # Type casting b to int
print(c)  # This will print 31

print(a + c)  # Now this will work because both are integers

# print(a + b)   not working because a is int and b is str
# Type casting b to int
b =  int(b)  # Type casting b to int
print(b)  # This will print 31

print(a + b)  # Now this will work because both are integers