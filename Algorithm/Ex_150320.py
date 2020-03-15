"""
There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time.
Given N, write a function that returns  the number of unique ways you can climb the staircase.
The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:
        1, 1, 1, 1
        2, 1, 1
        1, 2, 1
        1, 1, 2
        2, 2
What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive
integers X? For example, if X={1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
"""


def nums_way(n):
    if n == 0 or n == 1:
        return 1
    result = [0] * (n+1)
    result[0] = 1
    result[1] = 1
    for i in range(2, n+1):
        result[i] = result[i-1] + result[i-2]
    return result[n]


print(nums_way(5))

"""
Độ phức tạp O(n)
"""
