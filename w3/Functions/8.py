def spy(nums:list):
    s = ""

    for x in nums:
        s += str(x)

    if s.find("007") != -1:
        return True
    else:
        return False


list1 = [1,2,4,0,0,7,5] # True
list2 = [1,0,2,4,0,5,7] # True
list3 = [1,7,2,0,4,5,0] # False

print(spy(list3))