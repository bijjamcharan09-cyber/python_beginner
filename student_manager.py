FILE_NAME = "students.txt"

while True:
    print("\n===== MENU =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Calculate Average")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        marks = input("Enter marks: ")

        file = open(FILE_NAME, "a")
        file.write(name + "," + marks + "\n")
        file.close()

        print("Student record saved!")

    elif choice == "2":
        try:
            file = open(FILE_NAME, "r")

            print("\nStudent Records")
            for line in file:
                name, marks = line.strip().split(",")
                print("Name:", name, "| Marks:", marks)

            file.close()

        except FileNotFoundError:
            print("No records found.")

    elif choice == "3":
        try:
            file = open(FILE_NAME, "r")

            total = 0
            count = 0

            for line in file:
                name, marks = line.strip().split(",")
                total += int(marks)
                count += 1

            file.close()

            if count > 0:
                average = total / count
                print("Average Marks:", average)
            else:
                print("No student records.")

        except FileNotFoundError:
            print("No records found.")

    elif choice == "4":
        print("Program Ended.")
        break

    else:
        print("Invalid Choice!")
