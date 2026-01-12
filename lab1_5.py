def check_multiple(number):
    """Returns True if a number is a multiple of both 3 and 5, otherwise False."""
    if number % 3 == 0 and number % 5 == 0:
        return True
    else:
        return False

def check_password(input_string):
    """Checks if the input matches the secret word."""
    secret_word = "Python123"
    if input_string == secret_word:
        return "access granted"
    else:
        return "access denied"

def calculate_federal_tax(salary):
    """Calculates tax based on salary brackets using chained conditionals."""
    if salary <= 11000:
        tax = salary * 0.10
    elif salary <= 44725:
        tax = salary * 0.12
    elif salary <= 95375:
        tax = salary * 0.22
    else:
        tax = salary * 0.24
    
    return tax
