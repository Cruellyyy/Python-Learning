def salary(**kwargs):
    for item in kwargs.keys():
        print(f"The salary of {item} is: {kwargs[item]}")
        
salary(anvesh = 90, prince = 9999999999, rishabh = 92884 )
salarydict = {"anvesh": 90, "prince":9999293, "rishabh": 90009 }
salary(salarydict)