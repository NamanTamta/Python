# Simple calculator in One Line
# print(eval(input("Enter expression: ")))

# Calculator with functions
# Add Function
def add(x, y):
    return x + y
# Subtract Function
def subtract(x, y):
    return x - y
# Multiply Function
def multiply(x, y):
    return x * y
# Divide Function
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# User Input
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
op = input("Enter choice (1/2/3/4):")
num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))

# Perform operation based on user choice with If-Else statements

if op == '1':
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif op == '2':
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
elif op == '3':
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
elif op == '4':
    print(f"{num1} / {num2} = {divide(num1, num2)}")
    
