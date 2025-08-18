y = 10

def sum(a,b):
    c = a + b 
    y = 0  #creates seperate local vaiable and not affect the global var
    return 


sum(99,42)
print(y)



x = 10

def sum(a,b):
    ''' this function is used for adding a and b'''
    c = a + b
    global x   
    x = 0  #the keyword global allow us to change the global var inside an function
    return 

print(sum.__doc )

sum(99,42)
print(x)