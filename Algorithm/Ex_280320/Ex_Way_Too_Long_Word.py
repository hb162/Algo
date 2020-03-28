"""
Sometimes some words like "localization" or "internationalization" are so long
that writing them many times in one text is quite tiresome.

Let's consider a word too long, if its length is strictly more than 10 characters.
All too long words should be replaced with a special abbreviation.

This abbreviation is made like this:
we write down the first and the last letter of a word and between them we write the number of letters between the first
and the last letters.
That number is in decimal system and doesn't contain any leading zeroes.

Thus, "localization" will be spelt as "l10n", and "internationalization» will be spelt as "i18n".

You are suggested to automatize the process of changing the words with abbreviations.
At that all too long words should be replaced by the abbreviation and the words that are not too long should not undergo
 any changes.

"""


def abbreviation(word):
    sub = word[1:-1]
    length = len(sub)
    if length >= 10:
        sub = length
    else:
        return word
    sub = str(sub)
    word = word[0] + sub + word[-1]
    return word


n = int(input("Nhập số chữ:"))
words = []
while 1 <= n <= 1000:
    for i in range(n):
        word = input("Nhập chữ:").lower()
        words.append(word)
        n = n - 1

for word in words:
    print(abbreviation(word))

"""
Độ phức tạp: O(1)
"""