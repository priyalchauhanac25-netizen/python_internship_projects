import csv

# Student data
students = [
    ["Name", "Marks"],
    ["Priyal", 95],
    ["Badrinath", 94],
    ["Moulik", 91],
    ["Vedika", 92]
]

# Write data to CSV file
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)

print("Data written to students.csv successfully!")

# Read data from CSV file
print("\nReading data from CSV file:\n")

with open("students.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)