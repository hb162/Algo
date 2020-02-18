list = [4, 7, 1, -3, 2]


def two_sum(list, k):
    for i in list:
        for y in list:
            if i + y == k:
                return True
    return False


print(two_sum(list, 5))
