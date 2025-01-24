def search_text_in_file(file_path, search_text):
  with open(file_path, 'r') as file:
    lines = file.readlines()
  return [line for line in lines if search_text in line]

file_path = "Python.txt"
search_text = "Python"

print(search_text_in_file(file_path, search_text))