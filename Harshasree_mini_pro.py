# STUDENT PROGRESS TRACKER SYSTEM

def students_data():
    marks = []

    # Student Details
    name = input("Enter Student Name: ")
    student_class = input("Enter Student Class: ")
    rollno = input("Enter Student Roll Number: ")

    # Number of Subjects
    subs = int(input("\nHow many subjects do you want to enter? "))
    totalmarks = 0

    print()

    # Enter Marks
    for i in range(subs):
        mark = int(input(f"Enter marks for subject {i + 1}: "))
        marks.append(mark)
        totalmarks += mark

    # Calculations
    average = totalmarks / subs
    highest = max(marks)
    lowest = min(marks)
    percentage = (totalmarks / (subs * 100)) * 100

    # Grade Calculation
    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 50:
        grade = "C"
    elif average >= 35:
        grade = "D"
    else:
        grade = "Fail"

    # Pass / Fail Check
    status = "Pass"
    for m in marks:
        if m < 35:
            status = "Fail"
            grade = "Fail"
            break

    # Remarks
    if grade == "A":
        remarks = "Excellent"
    elif grade == "B":
        remarks = "Good"
    elif grade == "C":
        remarks = "Average"
    elif grade == "D":
        remarks = "Needs Improvement"
    else:
        remarks = "Needs Improvement"

    return (
        name,
        student_class,
        rollno,
        marks,
        totalmarks,
        average,
        highest,
        lowest,
        percentage,
        grade,
        status,
        remarks,
    )


# MAIN PROGRAM
while True:
    print("\n-------------------------------------------")
    print("        STUDENT PROGRESS TRACKER SYSTEM")
    print("-------------------------------------------\n")

    (
        name,
        student_class,
        rollno,
        marks,
        totalmarks,
        average,
        highest,
        lowest,
        percentage,
        grade,
        status,
        remarks,
    ) = students_data()

    print("\n---------- STUDENT REPORT -----------")
    print(f"Name            : {name}")
    print(f"Class           : {student_class.upper()}")
    print(f"Roll Number     : {rollno}")
    print(f"Highest Mark    : {highest}")
    print(f"Lowest Mark     : {lowest}")
    print(f"Total Marks     : {totalmarks}")
    print(f"Average Marks   : {average:.2f}")
    print(f"Percentage      : {percentage:.2f}%")
    print(f"Grade           : {grade}")
    print(f"Status          : {status}")
    print(f"Remarks         : {remarks}")
    print("-------------------------------------\n")

    print("What do you want to do next?\n")
    print("1. Enter marks again")
    print("2. View report again")
    print("3. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        continue

    elif choice == "2":
        print("\n---------- STUDENT REPORT -----------")
        print(f"Name            : {name}")
        print(f"Class           : {student_class.upper()}")
        print(f"Roll Number     : {rollno}")
        print(f"Highest Mark    : {highest}")
        print(f"Lowest Mark     : {lowest}")
        print(f"Total Marks     : {totalmarks}")
        print(f"Average Marks   : {average:.2f}")
        print(f"Percentage      : {percentage:.2f}%")
        print(f"Grade           : {grade}")
        print(f"Status          : {status}")
        print(f"Remarks         : {remarks}")
        print("-------------------------------------\n")

    elif choice == "3":
        print("Exiting... Thank you!")
        break

    else:
        print("Invalid Option! Try again.")
