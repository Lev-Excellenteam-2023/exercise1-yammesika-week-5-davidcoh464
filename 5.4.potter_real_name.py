import os
import zipfile

def extract_files(zip_path, extract_dest):
    zip_ref = zipfile.ZipFile(zip_path, 'r')
    zip_ref.extractall(extract_dest)
    zip_ref.close()

def find_real_name(local_file_path):
    file = open(local_file_path, 'r',errors="ignore")
    content = file.read()
    file.close()
    chapter_name = content.split("Chapter ")[1].split('<')[0].split(':')
    chapter_num = chapter_name[0]
    while len(chapter_num) < 3:
        chapter_num = '0' + chapter_num
    return chapter_num + chapter_name[1]

def extract_potter_and_rename(local_path):
    if not os.path.exists(os.path.join(local_path, 'potter')):
        extract_files(os.path.join(local_path, 'potter.zip'), os.path.join(local_path, 'potter'))
    
    local_path = os.path.join(local_path, 'potter')
    
    for file_name in os.listdir(local_path):
        end_file = file_name.split('.')[-1]
        file_real_name = find_real_name(os.path.join(local_path, file_name)) + '.' + end_file
        if not os.path.exists(os.path.join(local_path, file_real_name)):
            os.rename(os.path.join(local_path, file_name), os.path.join(local_path, file_real_name))

extract_potter_and_rename('C:/Users/User/Downloads/Notebooks-master/Notebooks-master/week05/resources')