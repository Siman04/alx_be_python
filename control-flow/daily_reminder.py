Task = input("Enter your task:")
Priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match Priority:
    case "high":
        if time_bound.lower() == "yes":
            print("Reminder to consider working on this project ASAP!")
        else :
            print("Consider completing this task  when you have free time.")
    case "medium":
        if  time_bound.lower() == "yes":
            print("Reminder this is a medium priority time bound task complete it soon!")
        else :
            print("Consider completing this task  when you have free time.")
    case "low":
        if  time_bound.lower() == "yes":
            print("Reminder this is a low priority time bound task complete it at your own time!")
        else :
            print(" no rush Consider completing this task  when you have free time.")