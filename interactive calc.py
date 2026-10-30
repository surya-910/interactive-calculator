
# Interactive Calculator & Unit Converter

def calculator():
    print("\n--- Basic Calculator ---")

    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            break
        except ValueError:
            print("Invalid input! Enter numbers only.")

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Choose operation (1-4): ")

    if choice == "1":
        print("Result:", num1 + num2)
    elif choice == "2":
        print("Result:", num1 - num2)
    elif choice == "3":
        print("Result:", num1 * num2)
    elif choice == "4":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error! Division by zero is not allowed.")
    else:
        print("Invalid operation!")


def unit_converter():
    print("\n--- Unit Converter ---")
    print("1. Kilometres to Miles")
    print("2. Celsius to Fahrenheit")

    choice = input("Choose conversion (1-2): ")

    while True:
        try:
            value = float(input("Enter value: "))
            break
        except ValueError:
            print("Invalid input! Enter a number.")

    if choice == "1":
        result = value * 0.621371
        print("Miles:", result)

    elif choice == "2":
        result = (value * 9/5) + 32
        print("Fahrenheit:", result)

    else:
        print("Invalid choice!")


def currency_converter():
    print("\n--- Currency Converter ---")
    print("1. INR to USD")
    print("2. USD to INR")

    choice = input("Choose conversion (1-2): ")

    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount < 0:
                print("Amount cannot be negative.")
                continue
            break
        except ValueError:
            print("Invalid input! Enter a number.")

    # Sample exchange rate; update when required.
    rate = 0.012

    if choice == "1":
        print("USD:", amount * rate)
    elif choice == "2":
        print("INR:", amount / rate)
    else:
        print("Invalid choice!")


# Main program
while True:
    print("\n==============================")
    print(" INTERACTIVE CALCULATOR")
    print("==============================")
    print("1. Basic Calculator")
    print("2. Unit Converter")
    print("3. Currency Converter")
    print("4. Exit")

    main_choice = input("Enter your choice (1-4): ")

    if main_choice == "1":
        calculator()

    elif main_choice == "2":
        unit_converter()

    elif main_choice == "3":
        currency_converter()

    elif main_choice == "4":
        print("Thank you for using the program!")
        break

    else:
        print("Invalid choice! Please try again.")
