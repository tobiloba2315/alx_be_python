class Calculator:
    # Class Attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Return the sum of two numbers."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Return the product of two numbers and print the class attribute."""
        print(f"Calculation Type: {cls.calculation_type}")
        return a * b


# Example usage (optional):
if __name__ == "__main__":
    print("Addition:", Calculator.add(5, 7))
    print("Multiplication:", Calculator.multiply(4, 3))
