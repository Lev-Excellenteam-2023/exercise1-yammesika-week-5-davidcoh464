from os import path
from os import listdir


def thats_the_way(dir_path: str, start_with: str) -> list:
    """
    Returns a list of files in a directory that start with the specified prefix.

    Args:
        dir_path (str): The path to the directory.
        start_with (str): The prefix that the files should start with.

    Returns:
        list: A list of file names that start with the specified prefix.

    Raises:
        ValueError: If the specified directory path does not exist.

    Examples:
        >>> thats_the_way('/path/to/directory', 'file')
        ['file1.txt', 'file2.txt']

    """
    if not path.exists(dir_path):
        raise ValueError("Path doesn't exist")

    return [file for file in listdir(dir_path) if file.startswith(start_with)]


if __name__ == "__main__":
    print(thats_the_way("C://Users//user//Downloads", "David"))
