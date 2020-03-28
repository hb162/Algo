"""
Vasily the Programmer loves romance, so this year he decided to illuminate his room with candles.

Vasily has a candles.When Vasily lights up a new candle, it first burns for an hour and then it goes out.
Vasily is smart, so he can make b went out candles into a new candle.
As a result, this new candle can be used like any other new candle.

Now Vasily wonders: for how many hours can his candles light up the room if he acts optimally well?
Help him find this number.
"""


def cal_hour(a, b):
    total_hour = a
    while a >= b:
        total_hour += (a/b)
        total_hour = int(total_hour)
        a = (a/b)
        a = int(a)
    return total_hour


print(cal_hour(123, 5))

"""
Độ phức tạp: O(n)
"""