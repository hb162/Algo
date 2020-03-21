"""
This problem was recently asked by Microsoft.

You 2 integers n and m representing an n by m grid,

determine the number of way you can get from the top-left to the bottom-right of the matrix y going only
right or down.

"""


def num_ways(m, n):
    count = [[0 for x in range(m)] for y in range(n)]
    for row in range(m):
        count[row][0] = 1
    for col in range(n):
        count[0][col] = 1
    for row in range(1, m):
        for col in range(n):
            count[row][col] = count[row-1][col] + count[row][col-1]
    print(count[m-1][n-1])


print(num_ways(2, 2))

"""
Độ phức tạp:O(mn)
"""