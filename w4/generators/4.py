def squares(a, b:int):
    i = 1

    while (i**2 <= b):
        if i **2 >= a:
            yield i**2
        i += 1

for i in squares(int(input()), int(input())):
    print(i, end=' ')
