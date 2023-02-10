def has_33(nums:list):
    cnt = 0

    for x in nums:
        if x == 3:
            cnt += 1
        else:
            cnt = 0
        
        if cnt == 2:
            return True
            break

    return False


list1 = [1, 3 , 3] # True
list2 = [1, 3 , 1 , 3]  # False
list3 = [3, 1 , 3] # False

print(has_33(list3))