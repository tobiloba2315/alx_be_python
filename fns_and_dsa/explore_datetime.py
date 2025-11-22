# explore_datetime.py


from datetime import datetime, timedelta


# Part 1: Function to display the current date and time
def display_current_datetime():
 current_date = datetime.now() 
 # Save current date and time
print("Current Date and Time:",current_date.strftime("%Y-%m-%d %H:%M:%S"))

# Part 2: Function to calculate a future date
def calculate_future_date(days):
 current_date = datetime.now()
future_date = current_date + timedelta(days=number_of_days) 
# Save future date
print("Future Date:", future_date.strftime("%Y-%m-%d"))

# Main Program Execution
if __name__ == "__main__":
 display_current_datetime()


# Ask user for number of days
try:
  days_to_add = int(input("\nEnter number of days to add:"))
  calculate_future_date(days_to_add)
except ValueError:
      print("Invalid input! Please enter an integer.")