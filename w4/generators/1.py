def square_n(n:int):
    i = 1

    while i <= n :
        yield i ** 2
        i += 1
    
for i in square_n(int(input())):
    print(i, end= " ")

