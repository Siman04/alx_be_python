task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")


match priority:
    case "high" | "High" | "HIGH":
        if time_bound.lower() == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. Complete it soon!")
    case "medium" | "Medium" | "MEDIUM":
        if time_bound.lower() == "yes":
            print(f"Reminder: '{task}' is a medium priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a medium priority task. Consider completing it when you have free time.")
    case "low" | "Low" | "LOW":
        if time_bound.lower() == "yes":
            print(f"Note: '{task}' is a low priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority entered. Please try again.")
