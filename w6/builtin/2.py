def count_upper_lower(s:str):
    upper_count = 0
    lower_count = 0

    for l in s:
        if l.isupper():
            upper_count += 1
        elif l.islower():
            lower_count += 1

    return (upper_count, lower_count)


s = input()
upper, lower = count_upper_lower(s)
print("Number of uppercase letters:", upper) 
print("Number of lowercase letters:", lower) 