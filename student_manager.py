FILE_NAME= "student.txt"


while True:
    print("_____\nMENU\n_____")
    print("1. Add Student")
    print("2. View Students")
    print("3. Calculate Average")
    print("4. Clear Records")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
            name = input("Enter student name: ")

            num_subjects = int(input("How many subjects? "))

            record = name

            for i in range(num_subjects):
                subject = input("Enter subject name: ")
                marks = input("Enter marks: ")

                record += "," + subject + ":" + marks

            file = open(FILE_NAME, "a")
            file.write(record + "\n")
            file.close()

            print("Student record saved!")

    elif choice == "2":
        try:
            file = open(FILE_NAME, "r")

            print("\nStudent Records")

            for line in file:
                data = line.strip().split(",")

                name = data[0]

                print("\nName:", name)

                for subject_data in data[1:]:
                    subject, marks = subject_data.split(":")
                    print(subject, ":", marks)

            file.close()

        except FileNotFoundError:
            print("No records found.")
    elif choice == "3":
        try:
            file = open(FILE_NAME, "r")

            for line in file:
                data = line.strip().split(",")

                name = data[0]

                total = 0
                count = 0

                for subject_data in data[1:]:
                    subject, marks = subject_data.split(":")
                    total += int(marks)
                    count += 1

                average = total / count

                print(f"{name}'s Average =", average)

            file.close()

        except FileNotFoundError:
            print("No records found.")
    elif choice == "5":
        print("Program Ended.")
        break
    elif choice == "4":
        confirm = input("Delete all records? (yes/no): ")

        if confirm.lower() == "yes":
            file = open(FILE_NAME, "w")
            file.close()
            print("All records deleted.")
        else:
            print("Operation cancelled.")

    else:
        print("Invalid Choice!")
