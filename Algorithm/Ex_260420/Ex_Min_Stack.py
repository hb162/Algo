"""
Design a simple stack that supports push, pop, top and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element
getMin() -- Retrieve the minimum element in the stack
"""


class Stack:
    stack = []
    min_stack = []

    def push(self, data):
        self.stack.append(data)
        if len(self.stack) == 1:
            self.min_stack.append(data)
        if data < self.min_stack[-1]:
            self.min_stack.append(data)
        self.min_stack.append(self.min_stack[-1])

    def pop(self):
        if self.stack is None:
            return None
        else:
            self.stack.pop()

    def getMin(self):
        if self.min_stack is None:
            return None
        return self.min_stack[-1]

    def top(self):
        if self.stack is None:
            return None
        return self.stack[-1]


s = Stack()
s.push(10)
s.push(30)
s.push(120)
s.push(20)
s.push(5)
print(s.top())
print(s.getMin())
"""
Độ phức tạp: O(1)
"""

