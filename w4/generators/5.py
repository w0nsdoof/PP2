def all_nums(n:int):
    i = n

    while i >= 0:
        yield i
        i -= 1

for i in all_nums(int(input())):
    print(i, end=" ")
