import os
import zipfile


def extract_files(zip_path: str, extract_dest: str):
    """
    Extracts files from a zip archive to a specified destination directory.

    Args:
        zip_path (str): The path to the zip archive.
        extract_dest (str): The destination directory to extract the files to.

    Returns:
        None

    """
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_dest)


def find_real_name(local_file_path: str) -> str:
    """
    Finds the real name of a file based on its content.

    The function reads the content of the file located at the given path,
    searches for the chapter name and number, and constructs a new filename
    in the format 'chapter_number:chapter_name'. The chapter number is
    zero-padded to three digits.

    Args:
        local_file_path (str): The path to the file.

    Returns:
        str: The real name of the file.

    """
    with open(local_file_path, 'r', errors="ignore") as file:
        content = file.read()

    chapter_name = content.split("Chapter ")[1].split('<')[0].split(':')
    chapter_num = chapter_name[0]
    while len(chapter_num) < 3:
        chapter_num = '0' + chapter_num

    return chapter_num + chapter_name[1]


def extract_potter_and_rename(local_path: str):
    """
    Extracts a zip archive and renames the extracted files based on their content.

    The function checks if the 'potter' directory already exists in the specified
    local path. If it doesn't exist, it extracts the 'potter.zip' file to create
    the 'potter' directory. Then, it iterates through the files in the 'potter'
    directory, extracts the real name using the find_real_name function, and
    renames the files accordingly.

    Args:
        local_path (str): The local path where the extraction and renaming should occur.

    Returns:
        None

    """
    potter_dir = os.path.join(local_path, 'potter')

    if not os.path.exists(potter_dir):
        extract_files(os.path.join(local_path, 'potter.zip'), potter_dir)

    for file_name in os.listdir(potter_dir):
        file_path = os.path.join(potter_dir, file_name)
        end_file = file_name.split('.')[-1]
        file_real_name = find_real_name(file_path) + '.' + end_file
        if not os.path.exists(os.path.join(potter_dir, file_real_name)):
            os.rename(file_path, os.path.join(potter_dir, file_real_name))


if __name__ == "__main__":
    extract_potter_and_rename('C:/Users/User/Downloads/Notebooks-master/Notebooks-master/week05/resources')
