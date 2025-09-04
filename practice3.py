# newpractice.py - Python practice for GitHub

# 1. Greeting
print("Hello! Let's practice Python with GitHub.")

# 2. Basic math
x = 15
y = 4
print(f"{x} + {y} = {x + y}")
print(f"{x} - {y} = {x - y}")
print(f"{x} * {y} = {x * y}")
print(f"{x} / {y} = {x / y}")

# 3. List iteration
colors = ["red", "green", "blue"]
print("Colors:")
for color in colors:
    print(f"- {color}")

# 4. Function example
def greet_user(name):
    return f"Welcome, {name}! Keep practicing Python."

name = input("Enter your name: ")
print(greet_user(name))

# 5. Simple conditional
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")
