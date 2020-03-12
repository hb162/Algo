"""
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""

#solution 1:ĐỆ QUY
def count_way(message, n, kq):
    if n == 0:
        return 1
    s = len(message) - n
    if message[s] == '0':
        return 0
    if kq[n] is not None:
        return kq[n]
    result = count_way(message, n - 1, kq)
    if n >= 2 and int(message[s:s+2]) <= 26:
        result += count_way(message, n-2, kq)
    kq[n] = result
    return result


def num_way(message):
    kq = [None] * (len(message)+1)
    return count_way(message, len(message), kq)


message = '121'
print(num_way(message))
"""
Độ phức tạp: O(n)
"""

#solution 2:


def num_way2(message):
    count = [0] * (len(message) + 1)
    count[0] = 1
    if 1 <= int(message[0]) <= 9:
        count[1] = 1
    else:
        count[1] = 0
    for i in range(2, len(count)):
        if 1 <= int(message[i - 1]) <= 9:
            count[i] += count[i - 1]
        if 10 <= int(message[i - 2:i]) <= 26:
            count[i] += count[i - 2]
    return count[-1]


message = '121'
print(num_way2(message))


"""
Độ phức tạp: O(n)
"""