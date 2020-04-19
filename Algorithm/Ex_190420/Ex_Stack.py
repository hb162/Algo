"""
Implement a stack that has the following methods:

+ push(val), which pushes an element onto the stack
+ pop(), which pops off and returns the topmost element of the stack.
If there are no elements in the stack, then it should throw an error or return null.
+ max(), which returns the maximum value in the stack currently. If there are no elements in the stack,
then it should throw an error or return null.
"""


class Stack:
    stack = []
    max_stack = []

    def push(self, data):
        self.stack.append(data)
        if len(self.stack) == 1:
            self.max_stack.append(data)
        if data > self.max_stack[-1]:
            self.max_stack.append(data)
        self.max_stack.append(self.max_stack[-1])

    def pop(self):
        if self.stack is None:
            return None
        else:
            self.stack.pop()

    def max(self):
        if self.max_stack is None:
            return None
        return self.max_stack[-1]


s = Stack()
s.push(10)
s.push(30)
s.push(120)
s.push(20)

print(s.max())
"""
Độ phức tạp: O(1)
"""