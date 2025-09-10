class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def __str__(self):
        return f"The name is {self.name} and salary is {self.salary}"
    def __len__(self):
        return len(str(self.salary))
    
e1 = employee("Anvesh", 10)
print(e1.name, e1.salary)
print(str(e1))  #does e1.__str__ function, here str is more specific and points to correct method which is __str__
print(f"The digits in {e1.name} salary is {len(e1)}")  #does e1.__len__ function. here len specify __len__ function



