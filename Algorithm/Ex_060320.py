"""
Given an array of integers,
return a new array such that each element at index i of the new array is the product of all the numbers in the original array
except the one at i
"""

list_1 = [3, 1, 2, 6, 7, 0]


# def product_list_1(list_1):
#     list_2 = [1] * len(list_1)
#     for i in range(len(list_1)):
#         for j in range(len(list_1)):
#             if i == j:
#                 continue
#             list_2[i] *= list_1[j]
#     return list_2
#
#
# print(product_list_1(list_1))


"""
Độ phức tạp O(n^2)
"""


def product_list_with_division(list_1):
    list_2 = [0] * len(list_1)
    product = 1
    count_zero = 0
    for i in range(len(list_1)):
        if list_1[i] == 0:
            count_zero += 1
    if count_zero > 1:
        return list_2
    elif count_zero == 1:
        for i in range(len(list_1)):
            if list_1[i] == 0:
                for j in range(len(list_1)):
                    if j == i and list_1[j] == 0:
                        continue
                    product *= list_1[j]
                list_2[i] = product
            else:
                list_2[i] = 0
        return list_2
    else:
        for i in range(len(list_1)):
            product *= list_1[i]
        for i in range(len(list_1)):
            list_2[i] = int(product/list_1[i])
        return list_2


list123 = [1, 2, 3, 0]
print(product_list_with_division(list123))


"""
Độ phức tạp: ................ 
:(
"""


def product_list(list1):
    left = [0]*len(list1)
    right = [0] * len(list1)
    list2 = [0] * len(list1)
    left[0] = 1
    for i in range(1, len(list1)):
        left[i] = list1[i-1] * left[i-1]

    right[len(list1) - 1] = 1
    for i in range(len(list1) -2, -1, -1):
        right[i] = list1[i+1] * right[i+1]

    for i in range(len(list1)):
        list2[i] = right[i] * left[i]
    return list2


print(product_list(list_1))


"""
Độ phức tạp O(n)
"""
