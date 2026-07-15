FILE_NAME= "student.txt"
def add_student():
    name = input("Enter student name: ").capitalize()
    num_subjects = int(input("How many subjects? "))
    record = name

    for i in range(num_subjects):
        subject = input("Enter subject name: ").capitalize()
        marks = input("Enter marks: ")
        credits = input("Enter credits for this subject: ")
        record += "," + subject + ":" + marks + ":" + credits

    with open(FILE_NAME, "a") as file:
        file.write(record + "\n")

    print("Student record saved!")

def view_students():
    try:
        with open(FILE_NAME, "r") as file:
            records = file.readlines()

            if not records:
                print("\nNo student records found.")
                return

            print("\n" + "=" * 15)
            print("STUDENT RECORDS")
            print("=" * 15)

            for student_no, line in enumerate(records, start=1):
                data = line.strip().split(",")
                name = data[0]

                print(f"\nStudent {student_no}")
                print("-" * 15)
                print(f"Name : {name}\n")
                for i, subject_data in enumerate(data[1:], start=1):
                    subject, marks, credits = subject_data.split(":")
                    print(f"{i}. Subject : {subject}")
                    print(f"   Marks   : {marks}")
                    print(f"   Credits : {credits}")

            print("\n" + "=" * 15)

    except FileNotFoundError:
        print("No records found.")
def calculate_average():
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                data = line.strip().split(",")
                name = data[0]
                total = 0
                count = 0
                for subject_data in data[1:]:
                    subject, marks, credits = subject_data.split(":")
                    total += int(marks)
                    count += 1
                average = total / count
                print(f"{name}'s Average =", average)
    except FileNotFoundError:
        print("No records found.")

def clear_records():
    confirm = input("Delete all records? (yes/no): ")
    if confirm.lower() == "yes":
        with open(FILE_NAME, "w") as file:
            pass
        print("All records deleted.")
    else:
        print("Operation cancelled.")

def calculate_sgpa():
    try:
        with open(FILE_NAME, "r") as file:

            for line in file:
                data = line.strip().split(",")

                name = data[0]

                total_points = 0
                total_credits = 0

                for subject_data in data[1:]:

                    subject, marks, credits = subject_data.split(":")

                    marks = int(marks)
                    credits = int(credits)

                    # Grade Point Calculation
                    if marks >= 90:
                        grade_point = 10
                    elif marks >= 80:
                        grade_point = 9
                    elif marks >= 70:
                        grade_point = 8
                    elif marks >= 60:
                        grade_point = 7
                    elif marks >= 50:
                        grade_point = 6
                    else:
                        grade_point = 0

                    total_points += grade_point * credits
                    total_credits += credits

                if total_credits > 0:
                    sgpa = total_points / total_credits
                    print(f"{name}'s SGPA = {sgpa:.2f}")
                else:
                    print(f"{name} has no subjects.")

    except FileNotFoundError:
        print("No records found.")

def delete_student():
    name_to_delete = input("Enter student name to delete: ")

    try:
        with open(FILE_NAME, "r") as file:
            records = file.readlines()

        found = False

        with open(FILE_NAME, "w") as file:
            for record in records:
                data = record.strip().split(",")

                if data[0].lower() != name_to_delete.lower():
                    file.write(record)
                else:
                    found = True

        if found:
            print("Student record deleted successfully.")
        else:
            print("Student not found.")

    except FileNotFoundError:
        print("No records found.")

def total_students():#calculate total students
    try:
        with open(FILE_NAME, "r") as file:
            records = file.readlines()
            total = len(records)
            if total == 0:
                print("No Student records found.")
            else:
                print(f"Total Students: {total}")
    except FileNotFoundError:
        print("No records found.")  

def search_student():
    name = input("Enter student name to search: ")

    try:
        with open(FILE_NAME, "r") as file:
            found = False

            for line in file:
                data = line.strip().split(",")

                if data[0].lower() == name.lower():
                    found = True
                    print("\nStudent Found")
                    print(" Name:", data[0])

                    for subject in data[1:]:
                        sub, marks, credits = subject.split(":")
                        print(f" Subject: {sub}\n Marks: {marks}\n Credits: {credits}")

            if not found:
                print("Student not found.")

    except FileNotFoundError:
        print("No records found.")  

def update_student():
    name_to_update = input("Enter student name to update: ")

    try:
        with open(FILE_NAME, "r") as file:
            records = file.readlines()

        found = False

        with open(FILE_NAME, "w") as file:
            for record in records:
                data = record.strip().split(",")

                if data[0].lower() == name_to_update.lower():
                    found = True

                    print("\nCurrent Record")
                    print("-" * 40)
                    print("Name:", data[0])

                    for i, subject_data in enumerate(data[1:], start=1):
                        subject, marks, credits = subject_data.split(":")
                        print(f"{i}. {subject} | Marks: {marks} | Credits: {credits}")
                    print("=" * 40)
                    print("\nEnter New Details")
                    print("=" * 40)

                    new_name = input("Enter new student name: ").capitalize()

                    while True:
                        try:
                            num_subjects = int(input("Enter number of subjects: "))
                            if num_subjects > 0:
                                break
                            print("Enter at least one subject.")
                        except ValueError:
                            print("Enter a valid number.")

                    new_record = new_name

                    for i in range(num_subjects):
                        print(f"\nSubject {i+1}")

                        subject = input("Subject Name : ").capitalize()

                        while True:
                            try:
                                marks = int(input("Marks (0-100): "))
                                if 0 <= marks <= 100:
                                    break
                                print("Marks must be between 0 and 100.")
                            except ValueError:
                                print("Enter valid marks.")

                        while True:
                            try:
                                credits = int(input("Credits : "))
                                if credits > 0:
                                    break
                                print("Credits must be greater than 0.")
                            except ValueError:
                                print("Enter valid credits.")

                        new_record += f",{subject}:{marks}:{credits}"

                    file.write(new_record + "\n")

                else:
                    file.write(record)

        if found:
            print("\nStudent record updated successfully.")
        else:
            print("\nStudent not found.")

    except FileNotFoundError:
        print("No records found.")

def main():
    print("=" *15 + "\nStudent Manager\n" +"=" *15)
    while True:
        print("-" *16 + "\n      MENU\n" +"-" *16)
        print("1. Add Student")
        print("2. View Students")
        print("3. Calculate Average")
        print("4. Clear Records")
        print("5. Calculate SGPA")
        print("6. Delete Student Record")
        print("7. Total Students")
        print("8. Search Student")
        print("9. Update Student Record")
        print("10. Exit")

        choice = input("Enter your choice(1-10): ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()
        elif choice == "3":
            calculate_average()
        elif choice == "4":
            clear_records()
        elif choice == "5":
            calculate_sgpa()
        elif choice == "6":
            delete_student()
        elif choice == "7":
            total_students()
        elif choice == "8":
            search_student()
        elif choice == "9":
            update_student()
        elif choice == "10":
            print("Program Ended.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted.")