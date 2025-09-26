def perform_operation(num1: float, num2: float, operation: str) -> float:

    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "cannot divide by zero"
        return num1 / num2
    else:
        return f"Error: unknown operation '{operation}'"
        raise ValueError(f"Unsupported operation '{operation}'. Supported operations are: add, subtract, multiply, divide.")