"""
Given a string of round, curly, and square open and closing brackets,
return whether the brackets are balanced (well-formed).

"""


def match_parenthensis(string):
    stack = []
    for i in range(len(string)):
        if string[i] == '(' or string[i] == '[' or string[i] == '{':
            stack.append(string[i])
            continue

        if len(stack) == 0:
            return False
        if string[i] == ')':
            top = stack.pop()
            if top == '{' or top == '[':
                return False
        elif string[i] == ']':
            top = stack.pop()
            if top == '(' or top == '{':
                return False
        elif string[i] == '}':
            top = stack.pop()
            if top == '(' or top == '[':
                return False

    if len(stack) == 0:
        return True
    return False


print(match_parenthensis("[]()}"))

"""
Độ phức tạp: O(n)
"""