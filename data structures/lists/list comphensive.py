#making a table containing multiples of 6
table_6 = []

for i in range(1, 10+1):
    table_6.append(6*i)

print(table_6)

#this is lengthy, we can don this in one line with comprehensive list

table_7 = [7*i for i in range(1,10+1)]
print(table_7)

while True:
    print("1")