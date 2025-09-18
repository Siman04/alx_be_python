num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Choose the operation (+, -, *, /): ")

match operator:
    case '+':
        result = num1 + num2
        print("The result is {}.".format(result))
    case '-':
        result = num1 - num2
        print("The result is {}.".format(result))
    case '*':
        result = num1 * num2
        print("The result is {}.".format(result))
    case '/':
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print("The result is {}.".format(result))
    case _:  # This is the correction
        print("Invalid operation.")
    
     

