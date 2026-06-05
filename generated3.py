# Addition function
def add_numbers(*args: float) -> float:
    """Return the sum of multiple numbers."""
    return sum(args)


# Subtraction function
def subtract_values(a: float, *args: float) -> float:
    """Return the difference of the first number and the subsequent numbers."""
    for b in args:
        a -= b
    return a


# Multiplication function
def multiply_inputs(*args: float) -> float:
    """Return the product of multiple numbers."""
    result = 1
    for num in args:
        result *= num
    return result


# Division function
def divide_elements(a: float, *args: float) -> float:
    """Return the division of the first number by the subsequent numbers. Handle division by zero."""
    for b in args:
        if b == 0:
            return "Error! Division by zero."
        a /= b
    return a


# Modulus function
def modulus_values(a: float, *args: float) -> float:
    """Return the modulus of the first number by the subsequent numbers. Handle modulus by zero."""
    for b in args:
        if b == 0:
            return "Error! Modulus by zero."
        a %= b
    return a


# Main calculator function
def calculator() -> None:
    """Run a simple calculator that performs various operations with up to 5 numbers."""
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
            numbers = [float(input(f"Enter number {i + 1}: ")) for i in range(5)]
        except ValueError:
            print("Invalid number input. Please enter numeric values.")
            continue

        op_name, op_func = operations[choice]
        result = op_func(*numbers)
        print(f"Result of {op_name}: {result}")

        next_calc = input("Do another calculation? (yes/no): ").strip().lower()
        if next_calc not in {"yes", "y"}:
            print("Calculator closed.")
            break


if __name__ == "__main__":
    calculator()