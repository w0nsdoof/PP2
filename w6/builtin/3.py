s = input()

if hash(s) == hash(s[::-1]):
    print("isPalindrome")
else:
    print("IsNotPalindrome")
