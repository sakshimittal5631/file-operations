import os

def search_text_in_file(file_path, search_text):
  with open(file_path, 'r') as file:
    lines = file.readlines()
  return [line for line in lines if search_text in line]

def search_text_in_folder(folder_path, search_text):
  results = {}
  for root, dirs, files in os.walk(folder_path):
    for file in files:
      file_path = os.path.join(root, file)

      try:
        matches = search_text_in_file(file_path, search_text)
        if matches:
          results[file_path] = matches
          break
      except Exception as e:
        print(f'Could not read {file_path}:{e}')
  print(results)

folder_path = "Demo"
search_text = "Python"

search_text_in_folder(folder_path, search_text)