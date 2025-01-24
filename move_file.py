import shutil

def move(src, dst):
  shutil.move(src, dst)
  print(f'File moved.')

src = "File3.txt"
dst = "./Demo"

move(src, dst)