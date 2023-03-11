import os

file = open("test.txt", "r")

data = file.read()

count_lines = data.count("\n")

print(count_lines + 1)