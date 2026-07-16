# Student Report Generator

# Taking student details
name = input("Enter student name: ")

marks = []

print("Enter marks for 5 subjects:")

for i in range(5):
    mark = float(input(f"Enter marks of subject {i+1}: "))
    marks.append(mark)

# Calculating result
total = sum(marks)
percentage = total / 5

# Grade calculation
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "F"

# Creating report
report = f"""
----------- Student Report -----------
Name: {name}

Marks:
Subject 1: {marks[0]}
Subject 2: {marks[1]}
Subject 3: {marks[2]}
Subject 4: {marks[3]}
Subject 5: {marks[4]}

Total Marks: {total}/500
Percentage: {percentage}%
Grade: {grade}

--------------------------------------
"""

print(report)

# Saving report into a file
with open("student_report.txt", "w") as file:
    file.write(report)

print("Report saved successfully!")