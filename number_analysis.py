# Read Numerical Data from File

filename = r"Notes/internship_tasks/Level4_Task_4/numbers.txt"

numbers = []

# Reading numbers from file
with open(filename, "r") as file:
    for line in file:
        numbers.append(int(line.strip()))

# Calculations
total = sum(numbers)
average = total / len(numbers)
maximum = max(numbers)

# Display result
print("------------------------")
print("Number Analysis Report")
print("------------------------")

print("Numbers:", numbers)
print("Total:", total)
print("Average:", average)
print("Maximum:", maximum)

print("------------------------")

# Saving result
with open("analysis_report.txt", "w") as file:
    file.write("Number Analysis Report\n")
    file.write("----------------------\n")
    file.write(f"Numbers: {numbers}\n")
    file.write(f"Total: {total}\n")
    file.write(f"Average: {average}\n")
    file.write(f"Maximum: {maximum}\n")

print("Analysis report saved successfully!")