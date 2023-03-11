import os

path = input("path: ")

print("File exists:", os.access(path, os.F_OK))
print("File readible", os.access(path, os.R_OK))
print("File writeable:", os.access(path, os.W_OK))
print("File executabill:", os.access(path, os.X_OK))
