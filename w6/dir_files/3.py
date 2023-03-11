import os

path = input("path: ")

if os.path.exists(path):
    if os.path.exists(path):
        print("directory :", os.path.dirname(path))
        print("file name :", os.path.basename(path))
else:
    print("Incorrect path")