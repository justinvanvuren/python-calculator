def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the result of subtracting b from a."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of a and b."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return the result of dividing a by b.

    Raises:
        ValueError: if b is 0.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def run_calculator():
    """Run a simple menu-driven calculator."""
    menu = """
Choose an operation:
1. Add
2. Subtract
3. Multiply
4. Divide
q. Quit
"""
    while True:
        print(menu)
        choice = input("Enter your choice: ").strip()

        if choice == "q":
            print("Goodbye!")
            break

        if choice in ("1", "2", "3", "4"):
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
            except ValueError:
                print("Please enter valid numbers.")
                continue

            if choice == "1":
                print(f"Result: {add(a, b)}")
            elif choice == "2":
                print(f"Result: {subtract(a, b)}")
            elif choice == "3":
                print(f"Result: {multiply(a, b)}")
            elif choice == "4":
                try:
                    print(f"Result: {divide(a, b)}")
                except ValueError as e:
                    print(f"Error: {e}")
        else:
            print("Invalid option. Please choose 1, 2, 3, 4, or q.")


if __name__ == "__main__":
    run_calculator()