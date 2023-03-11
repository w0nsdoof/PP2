import os

list = ["Lorem", "Ipsum" , "Neque" , "Estaqas"]

with open("test.txt", "w") as file:
    for s in list:
        file.write(s + "\n")

file.close()