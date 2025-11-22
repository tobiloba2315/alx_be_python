# Ask the user to input a positive integer
size = int(input("Enter the size of the pattern:"))
# Prompt the user to enter a positive integer
n = int(input("Enter a positive integer:"))

# Ensure the input is positive
if n > 0:
    # Use nested loops to print a square pattern
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()  # Move to the next line after each row
else:
    print("Please enter a positive integer.")

