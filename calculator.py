def calculate(num1, sign, num2):
    if sign == '+':
        return num1 + num2
    elif sign == '-':
        return num1 - num2
    elif sign == '*':
        return num1 * num2
    elif sign == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operator"
def main():
    print("Welcome to the Calculator!")
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            sign = input("Enter an operator (+, -, *, /): ")
            num2 = float(input("Enter the second number: "))
            result = calculate(num1, sign, num2)
            print(f"Result: {result}\n")
        except ValueError:
            print("Invalid input. Please enter numeric values.\n")
        
        continue_choice = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if continue_choice != "yes":
            print("Goodbye!")
            break
main()