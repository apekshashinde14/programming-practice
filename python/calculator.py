print("===== SIMPLE CALCULATOR =====")

while True:
    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5.Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid menu option.")
        continue

    if choice not in [1, 2, 3, 4, 5]:
        print("Invalid choice! Please select between 1 and 5.")
        continue
    if choice == 5:
        print("Exiting Calculator!!!")
        break
    else:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        if choice == 1:
            print("Result:", num1 + num2)

        elif choice == 2:
            print("Result:", num1 - num2)

        elif choice == 3:
            print("Result:", num1 * num2)

        elif choice == 4:
            if num2 != 0:
                print("Result:", num1 / num2)
            else:
                print("Cannot divide by zero!")

        else:
            print("Invalid choice!")