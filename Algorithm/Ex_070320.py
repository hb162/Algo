list1 = [3, 2, 1, 0]


def first_positive(list_1):
    length = len(list_1)
    if 1 not in list_1:
        return 1
    if list_1 == [1]:
        return 2
    for i in range(length):
        if list_1[i] <= 0 or list_1[i] > length:
            list_1[i] = 1
    for i in range(length):
        n = list_1[i]
        n = abs(n)
        if n == len(list_1):
            if list_1[0] > 0:
                list_1[0] = -list_1[0]
            continue
        elif list_1[n] > 0:
            list_1[n] *= -1

    for i in range(1, len(list_1)):
        if list_1[i] > 0:
            return i

    if list_1[0] > 0:
        return len(list_1)

    return len(list_1) + 1


print(first_positive(list1))
