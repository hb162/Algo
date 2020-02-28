def calculate(exp):
    nums = []
    sign = 1
    num = 0
    total = 0

    for i in exp:
        if i.isdigit():
            num = num + int(i)
            continue
        total += sign * num
        num = 0
        if i == "-":
            sign = -1
        elif i == "+":
            sign = 1
        elif i == "(":
            nums.append(total)
            nums.append(sign)
            sign = 1
            total = 0
        elif i == ")":
            total *= nums.pop()
            total += nums.pop()

    return total + sign * num


exp = "-3+(3-2)"
print(calculate(exp))
