import os
from os import path

def thats_the_way(dir_path, start_with):
    L = []
    if not path.exists(dir_path):
        raise ValueError("Path don't exsit")
    for file in os.listdir(dir_path):
        if file.startswith(start_with):
            L.append(file)
    return L

print(thats_the_way("C:/Users/User/Downloads/Notebooks-master/Notebooks-master/week05/images","deep"))
