# 1 4 7 9 10 11 15 16 17 97 201
# 1 7 11 17 97

def strToList(s):
    numbers = []

    num = ""

    for c in s:
        if c == ' ':
            numbers.append(int(num))
            num = ""
        else:
            num += c

    numbers.append(int(num))

    return numbers

def isPrime(n:int):
    for x in range(2,n):
        if(n % x == 0):
            return False
            break

    return True

string1 = input()

nums = strToList(string1) # list

primes = []

for n in nums:
    if isPrime(n):
        primes.append(n)

print(primes)
            
