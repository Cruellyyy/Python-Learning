salary = [50000, 64000, 200000, 90000]
mixed = [93984, "hello world", 92.23, True] #lists contains muteable mixed data of any type in same ordern

# list unpacking
grocery = ["milk", "spinach", "fish", "potatoes", "bananas", "apples"]
a,b,c,d,e,f = grocery
print(a,b,c,d,e,f)

print(salary[0:3])
print(mixed[0])

salary.append(98833) #add this number in the original list
print(salary)
salary.append(1000)
print(salary)

salary.pop(0)  #by default reomves the last data in the list using indexes
print(salary)

mixed.extend(salary) #add another list in existing list
print(mixed)

salary.reverse()   #reverse the order
print(salary)

salary.sort()  #sort in increasing order
print(salary)

salary.remove(1000) #remove the first matching value in the list only
print(salary)

salary.insert(2,999)  #add value before the index
print(salary)

salary.count(2)
print(salary)