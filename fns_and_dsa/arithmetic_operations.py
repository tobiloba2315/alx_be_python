# Define the arithmetic function
def perform_operation(num1, num2, operation):
 """
Performs basic arithmetic operations.


Parameters:
num1 (float): First number
num2 (float): Second number
operation (str): One of 'add','subtract','multiply','divide'


Returns:
float or str: Result of the operation or an error message
 """

 if operation =='add':
        return num1 + num2
 elif operation =='subtract':
        return num1 - num2
 elif operation == 'multiply':
        return num1 * num2
 elif operation == 'divide':
        if num2 == 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
 else:
        return "Error: Invalid operation"
 
from arithmetic_operations import perform_operation


print("=== Basic Arithmetic Calculator ===")


# Get user inputs
num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))


print("Choose an operation:add,subtract,multiply,divide")
operation = input("Enter the operation:").lower()


# Perform operation
result = perform_operation(num1,num2,operation)


# Display result
print(f"Result: {result}")