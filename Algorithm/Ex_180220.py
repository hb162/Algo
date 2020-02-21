list = [0, 1, 2, 5]


def two_sum(list, k):
    result = {}
    for i in range(0, len(list)):
        remain = k - list[i]
        if remain in result:
            return True
        else:
            result[list[i]] = i
    return False


print(two_sum(list, 4))
