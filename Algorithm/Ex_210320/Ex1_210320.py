"""
The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.
"""


import random
import math


def distance_two_point(x1, y1, x2, y2):
    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return distance


def create_random(n):
    point_list = []
    for x in range(n):
        x = random.randint(-10000, 10000)
        y = random.randint(-10000, 10000)
        point_list.append([x, y])
    return point_list


inside = 0
n = int(input("Nhập số điểm muốn thả: "))
points = create_random(n)
for i in points:
    if distance_two_point(i[0], i[1], 0, 0) <= 10000:
        inside = inside + 1

print('%0.6f' % (4 * inside / (n)))

"""
Độ phức tạp: O(n)
"""