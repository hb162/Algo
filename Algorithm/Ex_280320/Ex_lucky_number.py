"""
Petya loves lucky numbers.
We all know that lucky numbers are the positive integers whose decimal representations contain only

For example, numbers 47, 744, 4 are lucky and 5, 17, 467 are not.

Petya calls a number almost lucky, if it could be evenly divided by some lucky number.
Help him find out if the given number n almost lucky.
"""


def lucky_numbers(num):
    if 1 <= num <= 1000:
        if num % 4 == 0 or num & 7 == 0:
            return True
        while num > 0:
            if num % 10 == 4 or num % 10 == 7:
                return True
            num /= 10
            int(num)
    return None


num = int(input("Nhập số:"))
print(lucky_numbers(num))

"""
Độ phức tạp: O(1)
"""