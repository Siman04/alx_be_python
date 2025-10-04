def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)

        if den == 0:
            raise ZeroDivisionError

        result = num / den
        # Per the expected output, return the result as a string
        # formatted like a float, e.g., "2.0"
        return f"Expected Output: result of the division is {result:.2f}"

    except ValueError:
        return "Expected Output Error: Please enter numeric values only."
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except Exception as e:
        return f"Error: An unexpected error occurred: {e}"