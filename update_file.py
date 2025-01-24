def update_file(file_path, content=""):
  with open(file_path, 'a') as file:
    file.write(content)
  print(f'File updated:{file_path}')

file_path = "FromProgram/File5.txt"
update_file(file_path, "Hello to the World also.")