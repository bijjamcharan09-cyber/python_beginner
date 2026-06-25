import os
FILE_NAME = "students.txt"
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w") as file:
        pass
print("File is created")

while True:
    print("\n===== MENU =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Calculate Average")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")

        num_subjects = int(input("How many subjects? "))

        record = name

        for i in range(num_subjects):
            subject = input("Enter subject name: ")
            marks = input("Enter marks: ")

            record += "," + subject + ":" + marks

        with open(FILE_NAME, "a") as file:
            file.write(record + "\n")

        print("Student record saved!")

    elif choice == "2":
        try:
            with open(FILE_NAME, "r") as file:
                print("\nStudent Records")

                for line in file:
                    data = line.strip().split(",")
                    name = data[0]

                    print("\nName:", name)

                    for subject_data in data[1:]:
                        subject, marks = subject_data.split(":")
                        print(subject, ":", marks)

        except FileNotFoundError:
            print("No records found.")
    elif choice == "3":
        try:
            with open(FILE_NAME, "r") as file:
                for line in file:
                    data = line.strip().split(",")
                    name = data[0]

                    total = 0
                    count = 0

                    for subject_data in data[1:]:
                        subject, marks = subject_data.split(":")
                        total += int(marks)
                        count += 1

                    average = total / count if count else 0
                    print(name, "Average =", average)

        except FileNotFoundError:
            print("No records found.")
    elif choice == "4":
        print("Program Ended.")
        break

    else:
        print("Invalid Choice!")
