class Animal:
    gamer = "Morock gamer"
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name} makes a sound.")
    
class Dog(Animal): #as this dog class is a child class of animal, it inheritance every variable or function or anything from parent class automatically and we use functions and var from the animal class within the dog class
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    def speak(self):
        super().speak() #so as speak function exist in both parent and child class, if i use child class, i would be able to use the child version of speak not the parent version, but using super().speak, we can access speak from the parent class 
        print(f"{self.name}: Wooff!")  #this overwrites the speak function in the animal class



dog1 = Dog("Pookie", "Labra")
dog1.speak()
print(dog1.gamer)  #accesssing the code in class animal while in subcalss dog

'''class A:
    def f(self): print("A.f")

class B(A):
    def f(self): print("B.f")

b = B()
b.f()   # Python checks: B has f? yes -> B.f runs
Step-by-step when b.f() runs:

Check B for f → found → execute B.f(b).

If B didn’t have f, Python would check A.

If not found anywhere, error AttributeError.

Tip: “Override” just means the subclass method hides the parent’s method because Python finds subclass first.'''