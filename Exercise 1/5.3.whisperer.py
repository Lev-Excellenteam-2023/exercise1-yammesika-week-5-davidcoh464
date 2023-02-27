import re
def whisperer(local_path):
    file = open(local_path, 'rb')# open to read as bytes
    file_content = file.read() 
    file.close()
    decode_file = file_content.decode('utf-8', 'ignore') # decode the bytes into string
    regex = r"([a-z]{5,}!)" # regular expression that matching at least 5 letters and '!' in the end
    return re.findall(regex, decode_file)
        
local_path = 'C:/Users/User/Downloads/Notebooks-master/Notebooks-master/week05/resources/logo.jpg' 
print(whisperer(local_path)) # ['python!', 'isawesome!', 'welldone!', 'goodjob!']