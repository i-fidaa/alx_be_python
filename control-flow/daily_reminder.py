task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

def conditional_statement():
    if time_bound == "yes":
        print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
    else:
        print(f"Note: '{task}' is a {priority} priority task, consider completing it when you have free time.")

match priority:
    case "high":
        conditional_statement()
    case "medium":
        conditional_statement()
    case "low":
        conditional_statement()