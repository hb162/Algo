"""
Hi, here's your problem today. This problem was recently asked by Apple:

You are given two singly linked lists. The lists intersect at some node. Find, and return the node.

Note: the lists are non-cyclical

Example:
    A = 1 -> 2 -> 3 -> 4
    B = 6 -> 3 -> 4

This should return 3
"""


def intersection(headA, headB):
    a = headA
    b = headB
    while a is not None or b is not None:
        if a is not None:
            a = a.next
        else:
            headB = headB.next
        if b is not None:
            b = b.next
        else:
            headA = headA.next
    while headA != headB:
        headA = headA.next
        headB = headB.next
    return headA


class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def prettyPrint(self):
        c = self
        while c:
            print(c.val)
            c = c.next


a = Node(1)
a.next = Node(2)
a.next.next = Node(3)
a.next.next.next = Node(4)

b = Node(6)
b.next = a.next.next

c = intersection(a, b)
c.prettyPrint()

"""
Độ phức tạp của thuật toán: O(La + Lb)
La: độ dài của a
Lb: độ dài của b
"""