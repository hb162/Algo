def sortNums(num):
    num1 = 0
    num2 = 0
    num3 = 0
    for i in num:
        if i == 1:
            num1 += 1
        if i == 2:
            num2 += 1
        if i == 3:
            num3 += 1
    sort = [1] * num1 + [2] * num2 + [3] * num3
    return sort


print(sortNums([1, 3, 2, 2, 1, 1, 1]))

