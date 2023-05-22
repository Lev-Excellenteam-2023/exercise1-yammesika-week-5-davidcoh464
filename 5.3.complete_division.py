import math


def is_complete_division(num: int) -> bool:
    """
    Checks if a number is a complete division number.

    A complete division number is a number whose sum of divisors (excluding itself) is equal to the number.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if the number is a complete division number, False otherwise.

    Examples:
        >>> is_complete_division(6)
        True

        >>> is_complete_division(12)
        False

    """
    if num < 2:
        return False

    divisors_sum = 1
    sqrt_num = math.isqrt(num)

    # Iterate from 2 to the square root of num (inclusive)
    for index in range(2, sqrt_num + 1):
        if num % index == 0:
            # index is a divisor of num
            divisors_sum += index

            second_divisor = num // index
            if index != second_divisor:
                # Add the second divisor if it's different from index
                divisors_sum += second_divisor

    return divisors_sum == num


def all_complete_division():
    """
    Generator function that yields all complete division numbers.

    Yields:
        int: The next complete division number.

    Examples:
        >>> func = all_complete_division()
        >>> [next(func) for _ in range(5)] # after a long time
        [6, 28, 496, 8128, 33550336]
    """
    num = 2
    while True:
        if is_complete_division(num):
            yield num
        num += 1


if __name__ == "__main__":
    out_complete_division = all_complete_division()
    print([next(out_complete_division) for _ in range(4)])
