class student:
    school = "Carmel"  #class method varibale, info is shared with every class object and doesnot need any object attibute, info shared and access with every object in the class

    def __init__(self, name, classs):  #instance attribute, need self as 1st argument, unique to each object
        self.name = name
        self.classs = classs

    def show_details(self):
        print(f"Name of the student is {self.name} from {self.classs}")
    
    @classmethod  #class method function
    def changeSchool_name (clss, new_name):
        if new_name:
            school = new_name
        print(school)

    @staticmethod #doesnt require clss or self(object), its like normal function outside of class, we use this so we can group same logic function together, it doesnt require any clss or obj attirbutes or var
    def add(a,b):
        return a + b

print(student.school)  #class var call
s1 = student("Arsh", 12)
s1.show_details()  #instance method class
print(student.add(9,11))  #static method class
student.changeSchool_name("MCS")  #class method call