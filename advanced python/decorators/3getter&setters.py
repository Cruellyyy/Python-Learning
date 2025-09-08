class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    @property
    def full_name(self):
        return self.name
    
    @property
    def first_name(self):
        f = self.name.split(" ")
        return f[0]
    
    @first_name.setter
    def first_name(self, value):
        if value:
            f = self.name.split(" ")
            f[0] = value
            print(f"Name is set to {f[0]}")
            new_name = f"{f[0]} {f[1]}"
            self.name = new_name

e1 = employee("Prince Nagda", 999999)
print(e1.first_name)
e1.first_name = "Princes"
print(e1.name)