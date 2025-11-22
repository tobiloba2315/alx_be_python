# A simple calculator using match-case for operation selection
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
# Get the operation from the user
operation = input("Choose the operation (+, -, *, /): ")
# Perform the operation using match-case
match operation:
    case "+":
        print(f"Result: {num1 + num2}")
    case "-":
        print(f"Result: {num1 - num2}")
    case "*":
        print(f"Result: {num1 * num2}")
    case "/":
        if num2 == 0:
            print("Error: Cannot divide by zero")
        else:
            print(f"Result: {num1 / num2}")
    case _:
        print("The result is [result].")
