class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b == 0:
            return "Error: Division by zero ❌"
        return self.a / self.b


# Example usage
calc1 = Calculator(90, 100)
print("Addition:", calc1.add())
print("Subtraction:", calc1.subtract())
print("Multiplication:", calc1.multiply())
print("Division:", calc1.divide())
calc2 = Calculator(50, 0)
print("Addition:", calc2.add())
print("Division:", calc2.divide())
calc3 = Calculator(25, 5)
print("Multiplication:", calc3.multiply())
print("Division:", calc3.divide())  
print("Subtraction:", calc3.subtract())