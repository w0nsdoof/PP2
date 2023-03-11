file_orig = open("test.txt", "r")

file_copy = open("test2.txt", "w")

for i in file_orig:
    file_copy.write(i)