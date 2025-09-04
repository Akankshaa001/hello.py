# practice2.py - More Python practice

# 1. Print a message
print("Welcome to Python practice!")

# 2. Simple calculator
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input("Choose operation (+, -, *, /): ")

if operation == '+':
    print(f"{num1} + {num2} = {num1 + num2}")
elif operation == '-':
    print(f"{num1} - {num2} = {num1 - num2}")
elif operation == '*':
    print(f"{num1} * {num2} = {num1 * num2}")
elif operation == '/':
    if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("Cannot divide by zero!")
else:
    print("Invalid operation!")

# 3. List and loop example
fruits = ["apple", "banana", "cherry", "graphes"]
print("Fruits list:")
for fruit in fruits:
    print(f"- {fruit}")

# 4. Function example
def square(n):
    return n * n

num = int(input("Enter a number to square: "))
print(f"The square of {num} is {square(num)}")
