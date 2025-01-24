import os

def create_file(file_path, content=""):
  with open(file_path, 'w') as file:
    file.write(content)
    print(f'File created:{file_path}')

def create_folder(folder_path):
  os.makedirs(folder_path, exist_ok=True)
  print(f'Folder created:{folder_path}')

create_folder("FromProgram")
create_file("FromProgram/File5.txt","Hello Python")