class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        print(f"Calculation type: {Calculator.calculation_type}")
        return a * b