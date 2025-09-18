num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter an operator (+, -, *, /): ")
if operator == '+':
    result = num1 + num2
    print("The result is {}.".format(result))
elif operator == '-':
    result = num1 - num2
    print("The result is {}.".format(result))
elif operator == '*':
    result = num1 * num2
    print("The result is {}.".format(result))
elif operator == '/':
    if num2 == 0:
        print("Cannot divide by zero.")
    else:
        result = num1 / num2
        print("The result is {}.".format(result))

    
     

