Task = input("Enter your task:")
Priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match Priority .lower():
    case "high":
        if time_bound.lower() == "yes":
            print(f"Reminder: '{Task}' is a high Priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{Task}' is a high Priority task. Complete it soon!")
    case "medium":
        if time_bound.lower() == "yes":
            print(f"Reminder: '{Task}' is a medium Priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{Task}' is a medium Priority task. Consider completing it when you have free time.")
    case "medium":
        if time_bound.lower() == "yes":
            print(f"Reminder: '{Task}' is a low Priority task. Complete it soon!")
        else:
            print(f"Note: '{Task}' is a low Priority task. Consider completing it when you have freetime.")
    case _:
        print("Invalid priority entered. Please try again.")
