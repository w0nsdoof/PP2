import os

path = input("path: ")

directories = list()
files = list()

for i in os.listdir(path):
    if os.path.isdir(f"{path}/{i}"):
        directories.append(i)
    if os.path.isfile(f"{path}/{i}"):
        files.append(i)

print("\nAll directories:", directories , "\n")
print("All files:", files)

