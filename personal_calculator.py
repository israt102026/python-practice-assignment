# Practice Problem 1: Personal Information & Simple Calculator

name = input("Enter your name: ")
age = int(input("Enter your age: "))
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

print()
print(f"Hello, {name}! Your age is {age}.")
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")

if num2 == 0:
    print("Division: Cannot divide by zero")
else:
    division = num1 / num2
    print(f"Division: {division}")