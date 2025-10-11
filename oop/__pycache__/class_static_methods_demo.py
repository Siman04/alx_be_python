class Calculator:
    calculation_type = "Arithmetic operations"

    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def multiply(x, y):
        print(f"Calculation type: {Calculator.calculation_type}")
        return x * y