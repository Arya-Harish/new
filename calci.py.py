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

# Main calculator
def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
