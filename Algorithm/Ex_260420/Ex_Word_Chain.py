"""
Two words can be 'chained' if the last character of thee first word is the same as the first character of the 2nd word.

Given a list of words, determine if there is a way to 'chain' all the words in a circle.
"""


lst = ['apple', 'eggs', 'spam',]


def chainedWords(lst):
    for i in range(len(lst)-1):
        if lst[i][-1] != lst[i+1][0]:
            return False
    return True


print(chainedWords(lst))

"""
Độ phức tạp: O(n)
"""