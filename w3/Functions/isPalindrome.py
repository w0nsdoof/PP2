def isPalindrome(s:str):
    s2 = s[::-1]

    if s == s2:
        return True
    else:
        return False


print(isPalindrome(input()))