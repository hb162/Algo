"""
Given a sorted list of numbers, return a list of strings that represent all of the consecutive numbers.
"""


def findRangers(nums):
    res = []
    a = b = nums[0]
    for i in nums[1:]:
        if i == b+1 or i == b:
            b = i
        else:
            if a == b:
                res.append(a)
            else:
                res.append((a, b))
            a = b = i
    if a == b:
        res.append(a)
    else:
        res.append((a, b))
    return res


nums = [0, 2, 3, 5, 5, 6, 7, 8, 10]
print(findRangers(nums))

"""
Độ phức tạp: O(n)
"""
