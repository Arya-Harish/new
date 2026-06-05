def add_numbers(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b

def subtract_values(a: float, b: float) -> float:
    """Return the difference of two numbers."""
    return a - b

def multiply_inputs(a: float, b: float) -> float:
    """Return the product of two numbers."""
    return a * b

def divide_elements(a: float, b: float) -> float:
    """Return the division of a by b. Handle division by zero."""
    if b == 0:
        raise ValueError("Error! Division by zero.")
    return a / b

def modulus_values(a: float, b: float) -> float:
    """Return the modulus of a by b. Handle modulus by zero."""
    if b == 0:
        raise ValueError("Error! Modulus by zero.")
    return a % b

def get_operation_choice() -> str:
    """Prompt user for operation choice and return it."""
    print("\nSelect operation:")
    operations = {
        "1": "Add",
        "2": "Subtract",
        "3": "Multiply",
        "4": "Divide",
        "5": "Modulus",
    }
    
    for key, name in operations.items():
        print(f"{key}. {name}")
    
    choice = input("Enter choice (1/2/3/4/5): ").strip()
    if choice not in operations:
        print("Invalid choice. Please choose a valid operation.")
    
    return choice

def get_numbers() -> tuple:
    """Prompt user for two numbers and return them as a tuple."""
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            return num1, num2
        except ValueError:
            print("Invalid input. Please enter numeric values.")

def calculator() -> None:
    """Run a simple calculator that performs various operations."""
    operations = {
        "1": add_numbers,
        "2": subtract_values,
        "3": multiply_inputs,
        "4": divide_elements,
        "5": modulus_values,
    }

    while True:
        choice = get_operation_choice()
        if choice not in operations:
            continue

        num1, num2 = get_numbers()
        result = operations[choice](num1, num2)
        print(f"Result: {result}")

        next_calc = input("Do another calculation? (yes/no): ").strip().lower()
        if next_calc not in {"yes", "y"}:
            print("Calculator closed.")
            break

if __name__ == "__main__":
    calculator()