
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Error: Cannot divide by zero"

    def power(self):
        return self.num1 ** self.num2

    def root(self):
        if self.num1 >= 0 or self.num2 % 2 != 0:
            return self.num1 ** (1 / self.num2)
        elif self.num1 < 0 and self.num2 % 2 == 1:
            return -abs(self.num1) ** (1 / self.num2)
        else:
            raise ValueError("Error: Cannot calculate the root with negative base and even exponent")

    def perform_operation(self, operation):
        if operation == 'add':
            return self.add()
        elif operation == 'subtract':
            return self.subtract()
        elif operation == 'multiply':
            return self.multiply()
        elif operation == 'divide':
            return self.divide()
        elif operation == 'power':
            return self.power()
        elif operation == 'root':
            return self.root()
        else:
            return "Error: Invalid operation"


# Example usage:
while True:
    answer = input("do you want to quit? ")
    if answer == "quit":
        break
    
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide, power, root): ")

    calculator_instance = Calculator(num1, num2)
    result = calculator_instance.perform_operation(operation)
    print(f"Result: {result}")

    # Writing result to file
    with open("calculator_results.txt", "a") as file:
        file.write(f"{num1} {operation} {num2} = {result}\n")


