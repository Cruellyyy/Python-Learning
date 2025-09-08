#no control over internal variables, can accidentally be changed
'''class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

e1 = employee("Anvesh", 200)
print(e1.salary)
e1.salary = 150
print(e1.salary)'''

#using setters and getters
class employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary
    @property  #read only
    def name(self):
        return self._name
    @property
    def salary(self):
        return self._salary
    @name.setter  
    def name(self, value):
        if not value:
            print("Please enter a name")
        else:
            self._name = value
    @salary.setter
    def salary(self, value):
        if value <20:
            print("salary is too low")
        else: 
            self._salary = value
        
e1 = employee("Anvesh", 50)
while True:
    method = int(input("1. Change name \n2. Change salary\n"))
    if method ==1 :
        print(f"Current name is {e1.name}")
        value = input("Enter the name\n")
        e1.name = value
        print(e1.name)
    elif method ==2:
        print(f"Current salary is {e1.salary}")
        value = int(input("Enter the name\n"))
        e1.salary = value
        print(e1.salary)


'''Yes — you’ve nailed the concept 💯. Let me refine and break it down so it sticks in your head:

---

### 🔑 Without Getters/Setters

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name     # public
        self.salary = salary # public

e1 = Employee("Anvesh", 200)
e1.salary = -100  # <-- no restriction, allowed!
print(e1.salary)  # program now has bad/invalid state
```

👉 Direct access = **no control** → user/dev can unintentionally break program rules.

---

### 🔑 With Getters/Setters (`@property`)

```python
class Employee:
    def __init__(self, name, salary):
        self._name = name       # convention: private
        self._salary = salary

    @property
    def salary(self):          # getter
        return self._salary

    @salary.setter
    def salary(self, value):   # setter with control
        if value < 20:
            print("Salary too low, not allowed!")
        else:
            self._salary = value
```

👉 Now, `salary` **looks like a normal variable** (`e1.salary = 100`) but behind the scenes your **logic runs automatically**.

---

### ✅ Why `_` is used

* `_salary` is just a convention in Python (not real privacy like Java/C++).
* It signals: **“Hey, this is internal, don’t touch it directly.”**
* So the public-facing attribute is `salary` (with logic), while `_salary` is the raw internal storage.

---

### ✅ Where and Why to Use

1. **Validation** – check conditions before updating (salary must be > 20).
2. **Read-only attributes** – expose only a getter, no setter.
3. **Computed values** – e.g., return `full_name` dynamically from `first + last`.
4. **Consistency** – code outside doesn’t know/care if it’s raw storage or computed.

---

### 🔥 Summary in your words (cleaned up):

* Without getters/setters → **full uncontrolled access**.
* With `@property` and setters → **controlled access** (read-only, validation, computed values).
* `_variable` → internal storage, not meant to be touched directly.

---

⚡ Your program is actually a **perfect example**. You took the “dangerous” direct-access case and then showed how to add control using `@property`. That’s exactly why it exists.

---

Do you want me to also show you a **real-world analogy** (like how banks use getters/setters for your account balance)? It might make this concept click even harder.
'''