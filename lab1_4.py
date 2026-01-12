def calculate_average(num1, num2, num3):
    """Calculates and returns the average of three numbers."""
    average = (num1 + num2 + num3) / 3
    return average

def add_tax(bill_total):
    """Returns the bill total plus a 10% tax."""
    # 1.10 represents the original 100% plus 10% tax
    total_with_tax = bill_total * 1.10
    return total_with_tax

def greet_user(name):
    """Returns a greeting string using the provided name."""
    return f"Hello {name}"
