import sys

def fibonacci_recursive(n: int) -> int:
    """
    Calculate nth Fibonacci number using recursion
    Args:
        n: Position in Fibonacci sequence
    Returns:
        nth Fibonacci number
    """
    if not isinstance(n, int):
        raise ValueError("Input must be an integer.")

    if n < 0:
        raise ValueError("Input must be a non-negative integer.")

    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

    pass

def sum_of_digits_recursive(num: int) -> int:
    """
    Calculate sum of digits using recursion
    Args:
        num: Input integer
    Returns:
        Sum of digits
    """
    if not isinstance(num, int):
        print("Input must be an integer.")
        sys.exit(1)

    # Handle negative numbers by making them positive
    if num < 0:
        print(f"Input must be a non-negative integer. The number {abs(num)} will be used")
        num = abs(num)

    if num == 0:
        return 0
    else:
        return (num % 10) + sum_of_digits_recursive(num // 10)
    pass

def is_palindrome_number(num: int) -> bool:
    """
    Check if number is palindrome
    Args:
        num: Input integer
    Returns:
        True if palindrome, False otherwise
    """
    if not isinstance(num, int):
        print("Input must be an integer.")
        sys.exit(1)

    num_str = str(num)
    return num_str == num_str[::-1]
    pass