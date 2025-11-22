# Prompt for a single task
task = input("Enter your task:")
priority = input("priority(high/medium/low):").lower()
time_bound = input("Is it time-bound?(yes/no):").lower()

# Process the task using match case
match priority:
    case "high":
        reminder = f"Reminder:'{task}' is a HIGH priority task."
    case "medium":
        reminder = f"Reminder:'{task}' is a MEDIUM priority task."
    case "low":
        reminder = f"Reminder:'{task}' is a LOW priority task."
    case _:
        reminder = f"Reminder:'{task}' has an UNKNOWN priority."

# Modify the reminder if the task is time-bound
if time_bound == "yes":
    reminder += " This is a time-bound task that requires immediate attention today!"

# Print final customized reminder
print(f"Reminder:")
