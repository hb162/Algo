"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
"""


class Node(object):
    def __init__(self, value1):
        self.value1 = value1
        self.next = None

    def __str__(self):
        return self.value1

    def prettyPrint(self):
        c = self
        while c:
            print(c.value1)
            c = c.next


def merge(list):
    nodes = []
    head = point = Node(0)
    for l in list:
        while l:
            nodes.append(l.value1)
            l = l.next
    for x in sorted(nodes):
        point.next = Node(x)
        point = point.next
    return head.next


a = Node(9)
a.next = Node(1)
a.next.next = Node(5)

b = Node(1)
b.next = Node(3)

c = Node(2)
c.next = Node(6)


list = [a, b, c]

l = merge(list)
l.prettyPrint()
"""
Space complexity: O(n)
Time: O(), hàm sorted e chưa xác định đc thời gian của nó
"""