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

        >>> join(['Hello', 'World'], ['Open', 'AI'], separator=' ')
        ['Hello', 'World', ' ', 'Open', 'AI']

    """
    if not params:
        return None

    result_list = []
    for param in params:
        if not isinstance(param, (list, tuple)):
            raise TypeError(f"{param} is not iterable")

        result_list.extend(param)
        result_list.append(separator)

    if result_list:
        del result_list[-1]

    return result_list


if __name__ == "__main__":
    print(join([1, 2], [8], [9, 5, 6], separator='@'))
    print(join([1, 2], [8], [9, 5, 6]))
    print(join([1], 6, 7))
    print(join())
