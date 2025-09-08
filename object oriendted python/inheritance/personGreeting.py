class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greeting(self):
        print(f"Good evening everybody. My name is {self.name} and i am {self.age} years old. Its nice meeting u all.")

class Student(Person):
    def __init__(self, name, age, rollNo, Class):
        super().__init__(name, age)
        self.Class = Class
        self.rollNo = rollNo
    def greeting(self):
        print(f"Good morning to everyone present over here, I am {self.name} from class {self.Class}, roll number {self.rollNo}. I am gratefull that I get to meet u all.")

class Employee(Person):
    def __init__(self, name, age, idNo, post):
        super().__init__(name, age)
        self.idNo = idNo
        self.post = post
    def greeting(self):
        print(f"Good morning to everyone present over here, I am {self.name}, the {self.post} of this company.My id number is {self.idNo}. I am gratefull that I get to meet u all.")

person1 = Person("John", 34)
person1.greeting()
person2 = Student("Alice", 16, 23, "10th")
person2.greeting()
person3 = Employee("Bob", 45, 1001, "Manager")
person3.greeting()  