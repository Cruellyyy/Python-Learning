class employee:
    company = "HP"

    def get_salary(self): #in function, self refrences to the object
        return 466353
    
Prince = employee()
print(Prince.get_salary())
print(Prince.company)
