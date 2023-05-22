def join(*params, separator: str = '-') -> list:
    """
    Concatenates multiple iterables with a specified separator.

    Args:
        *params: Variable-length arguments representing iterables.
        separator (str, optional): Separator to be inserted between concatenated elements. Defaults to '-'.

    Returns:
        list: A list containing the concatenated elements from the input iterables.

    Raises:
        TypeError: If any of the input arguments is not iterable.

    Examples:
        >>> join([1, 2, 3], [4, 5, 6])
        [1, 2, 3, '-', 4, 5, 6]

        >>> join([1, 2], [8], [9, 5, 6], separator='@')
        [1, 2, '@', 8, '@', 9, 5, 6]

    """
    if not params:
        return None

    result_list = [element for param in params for element in param if isinstance(param, (list, tuple))]
    result_list.extend([separator] * (len(params) - 1))

    return result_list


if __name__ == "__main__":
    print(join([1, 2], [8], [9, 5, 6], separator='@'))
    print(join([1, 2], [8], [9, 5, 6]))
    print(join([1], 6, 7))
    print(join())
