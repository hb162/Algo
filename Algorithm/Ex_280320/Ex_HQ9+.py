"""
HQ9+ is a joke programming language which has only four one-character instructions:

"H" prints "Hello, World!",
"Q" prints the source code of the program itself,
"9" prints the lyrics of "99 Bottles of Beer" song,
"+" increments the value stored in the internal accumulator.
Instructions "H" and "Q" are case-sensitive and must be uppercase.
The characters of the program which are not instructions are ignored.

You are given a program written in HQ9+. You have to figure out whether executing this program will produce any output.

"""


def joke_program(word):
    n = len(word)
    if n == 0:
        return 'No'
    for i in word:
        if i == 'H' or i == 'Q' or i == '9':
            return 'Yes'
    return 'No'


print(joke_program('HQU'))
"""
Độ phức tạp: O(n)
"""