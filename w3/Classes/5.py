
def filter_prime(user:list):
    rev_result = []
    result = []

    for i in user:
        for j in range(2, i - 1):
            isDivides = lambda a, b : a % b == 0
            if isDivides(i, j) :
                rev_result.append(i)

    for i in user:
        if not (i in rev_result):
            result.append(i)

    return result

list = [1,2,3,4,5,11,13,19,34,37]

print(filter_prime(list))
