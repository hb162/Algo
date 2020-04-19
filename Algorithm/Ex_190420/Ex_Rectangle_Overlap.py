"""
A rectangle is represented as a list [x1, y1, x2, y2], where [x1, y1] are the coordinates of its bottom-left corner,
[x2, y2] are the coordinates of its top-right corner.

Two rectangles overlap if the area of their intersection is positive.
To be clear, two rectangles that only touch at the corner or edges do not overlap.

Given two(axis-aligned) rectangles, return whether they overlap.
"""


def is_overlap(rec1, rec2):
    if rec1[0] >= rec2[2] or rec2[0] >= rec1[2]:
        return False
    if rec1[1] >= rec2[3] or rec2[1] >= rec1[3]:
        return False
    return True


rec1 = [0, 0, 1, 1]
rec2 = [1, 0, 2, 1]
print(is_overlap(rec1, rec2))

"""
Độ phức tạp: O(1)
"""