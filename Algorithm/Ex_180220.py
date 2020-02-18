list1 = [1, 5]


def two_sum(list1, k):
    for i in list1:
        for y in list1:
            if i + y == k:
                return True
    return False


print(two_sum(list1, 6))
