import random
from datetime import datetime


def string_to_date(str_date: str) -> datetime:
    """
    Converts a string date in the format 'YYYY-MM-DD' to a datetime object.

    Args:
        str_date (str): The string representation of the date.

    Returns:
        datetime: The datetime object representing the date.

    Raises:
        ValueError: If the input string is not in the correct format or represents an invalid date.

    Examples:
        >>> string_to_date('2023-05-17')
        datetime.datetime(2023, 5, 17, 0, 0)

    """
    try:
        return datetime.strptime(str_date, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Invalid date format: YYYY-MM-DD")


def vinaigrette(start_date: str, end_date: str) -> str:
    """
    Generates a random date within the specified date range and checks if it falls on a Monday.

    Args:
        start_date (str): The start date in the format 'YYYY-MM-DD'.
        end_date (str): The end date in the format 'YYYY-MM-DD'.

    Returns:
        str: A string representation of the randomly generated date in the format 'YYYY-MM-DD'.

    Raises:
        ValueError: If the start date or end date not in format of 'YYYY-MM-DD'.
        ValueError: If the start date is greater than the end date.

    Examples:
        >>> vinaigrette('2023-05-17', '2023-05-31')
        '2023-05-25'

    """
    start_date = string_to_date(start_date)
    end_date = string_to_date(end_date)

    if start_date > end_date:
        raise ValueError("Start date cannot be greater than end date")

    random_date = start_date + (end_date - start_date) * random.random()
    if random_date.weekday() == 0:
        print("Don't have vinaigrette!")

    return str(random_date.date())


if __name__ == "__main__":
    print(vinaigrette('1950-06-23', '2000-06-07'))
