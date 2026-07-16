students = {}

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Statistics")
    print("7. Exit")

    choice = input("Enter your choice: ")

    # Add Student
    if choice == "1":
        name = input("Enter student name: ")
        marks = float(input("Enter student marks: "))
        students[name] = marks
        print("Student added successfully!")

    # View Students
    elif choice == "2":
        if students:
            print("\nStudent Records:")
            for name, marks in students.items():

                if marks >= 90:
                    grade = "A+"
                elif marks >= 80:
                    grade = "A"
                elif marks >= 70:
                    grade = "B"
                elif marks >= 60:
                    grade = "C"
                else:
                    grade = "D"

                print(f"Name: {name}")
                print(f"Marks: {marks}")
                print(f"Grade: {grade}")
                print("-----------------------")
        else:
            print("No student records found.")

    # Search Student
    elif choice == "3":
        name = input("Enter student name to search: ")

        if name in students:
            marks = students[name]

            if marks >= 90:
                grade = "A+"
            elif marks >= 80:
                grade = "A"
            elif marks >= 70:
                grade = "B"
            elif marks >= 60:
                grade = "C"
            else:
                grade = "D"

            print(f"\n{name} found!")
            print(f"Marks: {marks}")
            print(f"Grade: {grade}")
        else:
            print("Student not found.")

    # Update Student
    elif choice == "4":
        name = input("Enter student name to update: ")

        if name in students:
            new_marks = float(input("Enter new marks: "))
            students[name] = new_marks
            print("Student updated successfully!")
        else:
            print("Student not found.")

    # Delete Student
    elif choice == "5":
        name = input("Enter student name to delete: ")

        if name in students:
            del students[name]
            print("Student deleted successfully!")
        else:
            print("Student not found.")

    # Statistics
    elif choice == "6":
        if students:
            total_students = len(students)
            highest_marks = max(students.values())
            lowest_marks = min(students.values())
            average_marks = sum(students.values()) / total_students

            print("\n===== Statistics =====")
            print("Total Students:", total_students)
            print("Highest Marks:", highest_marks)
            print("Lowest Marks:", lowest_marks)
            print("Average Marks:", round(average_marks, 2))
        else:
            print("No student data available.")

    # Exit
    elif choice == "7":
        print("Thank you for using Student Management System!")
        break

    else:
        print("Invalid choice! Please enter a number from 1 to 7.")