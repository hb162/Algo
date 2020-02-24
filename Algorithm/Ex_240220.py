def singleNumber(nums):
    my_set1 = set()
    my_set2 = set()
    for i in nums:
        if i not in my_set1:
            my_set1.add(i)
        else:
            my_set2.add(i)
    single = my_set1 ^ my_set2
    return single


print(singleNumber([4, 3, 2, 4, 1, 3, 2]))
