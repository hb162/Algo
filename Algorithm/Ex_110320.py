"""
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers.
Numbers can be 0 or negative.
Follow-up: Can u do this in O(n) time & constant space.
"""

my_list = [2, 5, 3, 1, 7]


def largest_sum(list):
    include = 0
    exclude = 0
    for i in range(len(list)):
        if exclude > include:
            temp = exclude
        else:
            temp = include
        include = list[i] + exclude
        exclude = temp

    if include > exclude:
        return include
    else:
        return include


print(largest_sum(my_list))
"""
Độ phức tạp O(n): n là độ dài của list
"""