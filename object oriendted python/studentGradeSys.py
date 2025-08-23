class students:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("")
        print("Name =", self.name)
        print("Marks =",self.marks)

    def check_pass_fail(self):
        if (self.marks < 40):
            print(self.name, "has failed in his exam")
        elif (self.marks >= 40):
            print(self.name, "has passed the exam")

Arsh = students("Arsh Khan", 89)
Prince = students("Prince Nagda", 60)
Anvesh = students("Anvesh Bhatta", 36)
Aniket = students("Aniket Patidar", 67)

Aniket.display()
Aniket.check_pass_fail()

Anvesh.display()
Anvesh.check_pass_fail()

Prince.display()
Prince.check_pass_fail()

Arsh.display()
Arsh.check_pass_fail()
