def func(n:int):
    i = 1

    while i <= n :
        if i % 12 == 0 :
            yield i
        i += 1

for i in func(int(input())):
    print(i, end= " ")
