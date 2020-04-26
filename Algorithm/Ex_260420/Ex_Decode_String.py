"""
Given a string with a certain rule: k[string] should be expanded to string k times. So for example,
3[abc] should be expanded to abcabcabc.
Nested expansions can happen, so 2[a2[b]c] should be expanded to abbcabbc.
"""


def decodeString(string):
    stack = []
    current_count = 0
    current_string = ""
    for i in string:
        if i == '[':
            stack.append(current_string)
            stack.append(current_count)
            current_string = ''
            current_count = 0
        elif i == ']':
            count = stack.pop()
            prev_string = stack.pop()
            current_string = prev_string + count*current_string
        elif i.isdigit():
            current_count = current_count*10 + int(i)
        else:
            current_string += i
    return current_string


print(decodeString("3[a2[b]c]"))
"""
Độ phức tạp: O(n)
"""