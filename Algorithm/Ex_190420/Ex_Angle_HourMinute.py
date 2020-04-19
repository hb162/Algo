"""
Given a time in the format of hour and minute, calculate the angle of the hour and minute hand on a clock.
"""


def calcAngle(h, m):
    if h < 0 or m < 0 or h > 12 or m > 60:
        return None
    if h == 12:
        h = 0
    if m == 60:
        m = 0
    hour_angle = (h * 60 + m) * 0.5
    minute_angle = 6 * m
    angle = abs(hour_angle - minute_angle)
    return angle


print(calcAngle(12, 30))

"""
Độ phức tạp: O(1)
"""