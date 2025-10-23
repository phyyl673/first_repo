def greet(name):
    """
    Prints a personalized greeting message for the given name.
    Example:
        >>> greet("Chris")
        Hello, Chris! Welcome to our team repository.
    """
    print(f"Hello, {name}! Welcome to our team repository.")

def generate_mystery_number(seed):
    import random
    random.seed(seed * 42)
    return (random.randint(1, 100) ** 2) % 77
