# Practice Problem 2: Student Grade Calculator

name = input("Enter student name: ")
math = float(input("Enter Math marks: "))
english = float(input("Enter English marks: "))
python = float(input("Enter Python marks: "))

marks = [math, english, python]

if any(m < 0 or m > 100 for m in marks):
    print("Invalid marks! Marks must be between 0 and 100.")
else:
    average = sum(marks) / 3

    if average >= 80:
        grade = "A+"
    elif average >= 70:
        grade = "A"
    elif average >= 60:
        grade = "A-"
    elif average >= 50:
        grade = "B"
    elif average >= 40:
        grade = "C"
    else:
        grade = "F"

    print()
    print(f"Student Name: {name}")
    print(f"Average Marks: {average:.2f}")
    print(f"Final Grade: {grade}")