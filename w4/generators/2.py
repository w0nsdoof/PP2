def even_n(n:int):
    i = 0

    while i <= n :
        yield i
        i += 2

for i in even_n(int(input())):
    print(i, end=",")