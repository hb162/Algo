"""
There are n people lined up, and each have a height represented as an integer.

A murder has happened right in front of them, and only people who are taller than everyone in front of them are
able to see what has happened. How many witnesses are there?

"""


def witnesses(heights):
    count = 1
    n = len(heights)
    max = heights[n-1]
    for i in range(n-1, -1, -1):
        if heights[i] <= 0:
            continue
        if heights[i] > max:
            max = heights[i]
            count = count+1
    return count


heights = [0, 0, 2, 5, 1]
print(witnesses(heights))

"""
Độ phức tạp: O(n)
"""