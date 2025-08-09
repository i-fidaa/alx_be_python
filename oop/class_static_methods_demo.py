class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static method: doesn't need access to class or instance data."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method: has access to class-level attributes via cls."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
