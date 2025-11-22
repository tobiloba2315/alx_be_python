# Ask the user to input a positive integer
size = int(input("Enter the size of the pattern:"))
# Prompt the user to enter a positive integer
n = int(input("Enter a positive integer:"))

# Ensure the number is positive
if size > 0:
    row = 0

    # While loop to iterate through each row
    while row < size:
        # For loop to print asterisks in each row
        for col in range(size):
            print("*", end="")

        # Print a newline after each row
        print()

        # Move to the next row
        row += 1

else:
    print("Error: Please enter a positive integer.")
