"""
A look-and-say sequence is defined as the integer sequence beginning with a single digit in which
the next term is obtained by describing the previous term.
"""


def find_nth(n):
    if n == 1:
        return "1"
    prev = find_nth(n-1)
    result = ""
    count = 1
    for i in range(len(prev)):
        if i == len(prev)-1 or prev[i] != prev[i+1]:
            result = result + str(count) + prev[i]
            count = 1
        else:
            count = count + 1
    return result


print(find_nth(4))

"""
Độ phức tạp: O(n)
"""