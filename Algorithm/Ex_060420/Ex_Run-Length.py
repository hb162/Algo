"""
Run-length encoding is a fact and simple method of encoding strings.
The basic idea is to represent repeated successive characters as a single count and character.
For ex, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. U can assume the string to be encoded have no digigts
and consists solely of alphabetic characters. You can assume the string to be decoded is valid.
"""


def run_length_encoding(s):
    n = len(s)
    count = 0
    code = ''
    for i in range(n):
        char = s[i]
        count += 1
        if i == n-1:
            code = code + str(count) + char
            break
        else:
            if char == s[i+1]:
                pass
            else:
                code = code + str(count) + char
                count = 0
    return code


print(run_length_encoding('AAAABBCADU'))

"""
Độ phức tạp: o(n)
"""