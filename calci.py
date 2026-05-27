# Addition function
def add_numbers(a, b):
    return a + b


# Subtraction function
def subtract_values(a, b):
    return a - b


# Multiplication function
def multiply_inputs(a, b):
    return a * b


# Division function
def divide_elements(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b


# Modulus function
def modulus_values(a, b):
    if b == 0:
        return "Error! Modulus by zero."
    return a % b


# Main calculator
def calculator():
    operations = {
        "1": ("Add", add_numbers),
        "2": ("Subtract", subtract_values),
        "3": ("Multiply", multiply_inputs),
        "4": ("Divide", divide_elements),
        "5": ("Modulus", modulus_values),
    }

    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")

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
