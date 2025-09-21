task = input("Enter your task:")
Priority = input("Priority (high/medium/low)")
time_bound = input("is it timebound?(yes/no)")

match Priority:
    case "high":
        if task is time_bound:
            print("Reminder to consider working on this project ASAP!")
        else :
            print("Consider completing this task  when you have free time.")
    case "medium":
        if task is time_bound:
            print("Reminder to consider working on this project ASAP!")
        else :
            print("Consider completing this task  when you have free time.")
    case "low":
        if task is time_bound:
            print("Reminder to consider working on this project ASAP!")
        else :
            print("Consider completing this task  when you have free time.")