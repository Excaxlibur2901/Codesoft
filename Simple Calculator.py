#CodSoft Internship Simple Calculator

while True:
    print("\n--- Vipul's Calculator ---")
    
    # Take inputs
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid number input. Try again.")
        continue

    # Operation choice
    print("\nChoose operation:")
    print("+  Addition")
    print("-  Subtraction")
    print("*  Multiplication")
    print("/  Division")
    print("AC / OFF  Exit Calculator")

    choice = input("Enter operation: ").upper()

    # Exit condition
    if choice in ["AC", "OFF"]:
        print("Calculator turned OFF.")
        break

    # Perform calculation
    if choice == '+':
        print("Result:", num1 + num2)

    elif choice == '-':
        print("Result:", num1 - num2)

    elif choice == '*':
        print("Result:", num1 * num2)

    elif choice == '/':
        if num2 == 0:
            print("Error: Division by zero.")
        else:
            print("Result:", num1 / num2)

    else:
        print("Invalid operation. Try again.")