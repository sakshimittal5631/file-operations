import os

def rename(old, neww):
  os.rename(old, neww)
  print(f'File renamed.')

old = "FileNo3"
neww = "File3.txt"

rename(old, neww)