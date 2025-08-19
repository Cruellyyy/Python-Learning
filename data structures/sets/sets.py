s =  {41,11,14,25,21,455,11,14,21} #output{25, 21, 455, 41, 11, 14} <class 'set'>, cuz no dublicates allowd so removed
print(s,type(s)) 
# print(s[2]) #error, cant do index cuz they are just collection of unordered unique data

s.add(93)
s.discard("ehefhb ") #not throw error if not present in the set
s.remove(11) #thows an error if not present
