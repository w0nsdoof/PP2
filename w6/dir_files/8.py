import os

path = input("path: ")

print("Exists:", os.path.exists(path))

if os.path.exists(path):
    print("Deletable:", os.access(path, os.W_OK))
    
    if os.access(path, os.W_OK):
        os.remove(path)
        print("Done")