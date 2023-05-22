import re


def whisperer(path: str) -> list:
    """
    Extracts whispered words from a file.

    The function reads the content of the file located at the given path,
    decodes it as a UTF-8 encoded string, and searches for whispered words,
    which are defined as sequences of at least 5 lowercase letters followed
    by an exclamation mark '!'. The function returns a list of all the
    whispered words found in the file.

    Args:
        path (str): The path to the file to read.

    Returns:
        list: A list of whispered words found in the file.
    """
    # Open the file to read as bytes
    with open(path, 'rb') as file:
        file_content = file.read()

    # Decode the bytes into a string
    decoded_file = file_content.decode('utf-8', 'ignore')

    # Regular expression pattern matching at least 5 lowercase letters followed by '!'
    pattern = r"([a-z]{5,}!)"

    # Find all occurrences of whispered words in the decoded file
    whispered_words = re.findall(pattern, decoded_file)
    # ['python!', 'isawesome!', 'welldone!', 'goodjob!']
    return whispered_words


if __name__ == "__main__":
    local_path = 'C:/Users/User/Downloads/Notebooks-master/Notebooks-master/week05/resources/logo.jpg'
    print(whisperer(local_path))
    # ['python!', 'isawesome!', 'welldone!', 'goodjob!']
