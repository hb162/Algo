"""
You are given an array of integers.

Return the largest product that can be made by mutiplying any 3 integers in the array.
"""


def largest_product(list):
    if len(list) <= 2:
        return None
    max_index1 = 0
    max_index2 = -1
    max_index3 = -1
    for i in range(1, len(list)):
        if list[i] > list[max_index1]:
            max_index3 = max_index2
            max_index2 = max_index1
            max_index1 = i
        elif list[i] > list[max_index2] or max_index2 == -1:
            max_index3 = max_index2
            max_index2 = i
        elif list[i] > list[max_index3] or max_index3 == -1:
            max_index3 = i
    min_index1 = 0
    min_index2 = -1
    for i in range(1, len(list)):
        if list[i] < list[min_index1]:
            min_index2 = min_index1
            min_index1 = i
        elif list[i] < list[min_index2] or min_index2 == -1:
            min_index2 = i

    result = max(list[max_index1] * list[max_index2] * list[max_index3],
                 list[min_index1] * list[min_index2] * list[max_index1])
    return result


list = [0, 0, -1, 1, 5]
print(largest_product(list))

"""
Độ phức tạp: O(n)
"""