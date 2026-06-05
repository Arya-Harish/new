# Addition function
def add_numbers(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


# Subtraction function
def subtract_values(a: float, b: float) -> float:
    """Return the difference of two numbers."""
    return a - b


# Multiplication function
def multiply_inputs(a: float, b: float) -> float:
    """Return the product of two numbers."""
    return a * b


# Division function
def divide_elements(a: float, b: float) -> float:
    """Return the division of a by b. Handle division by zero."""
    if b == 0:
        return "Error! Division by zero."
    return a / b


# Modulus function
def modulus_values(a: float, b: float) -> float:
    """Return the modulus of a by b. Handle modulus by zero."""
    if b == 0:
        return "Error! Modulus by zero."
    return a % b


# Main calculator function
def calculator() -> None:
    """Run a simple calculator that performs various operations."""
    operations = {
        "1": ("Add", add_numbers),
        "2": ("Subtract", subtract_values),
        "3": ("Multiply", multiply_inputs),
        "4": ("Divide", divide_elements),
        "5": ("Modulus", modulus_values),
    }

    while True:
        print("\nSelect operation:")
        for key, (name, _) in operations.items():
            print(f"{key}. {name}")

        choice = input("Enter choice (1/2/3/4/5): ").strip()
        if choice not in operations:
            print("Invalid input. Please choose a valid operation.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid number input. Please enter numeric values.")
            continue

        op_name, op_func = operations[choice]
        result = op_func(num1, num2)
        print(f"Result of {op_name}: {result}")

        next_calc = input("Do another calculation? (yes/no): ").strip().lower()
        if next_calc not in {"yes", "y"}:
            print("Calculator closed.")
            break


if __name__ == "__main__":
    calculator()