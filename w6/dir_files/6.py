import os

path = input()

for i in range(65, 91):
    filename = os.path.join(path, chr(i) + ".txt") 
    open(filename, "w").close()