"""
Given a singly linked lít and an integer k, remove the kth last element from the list.
k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohubitively expensive.

Do this in constant space and in one pass
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __int__(self):
        return self.data


def remove_kth_last(head, n):
    ptr1 = head
    ptr2 = head
    if head is None or head.next is None:
        return None
    for x in range(n):
        if ptr1 is None:
            return None
        ptr1 = ptr1.next
    while ptr1.next is not None:
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    ptr2.next = ptr2.next.next
    return head


def print_list(head):
    while head is not None:
        print(head.data, end=' ')
        head = head.next


a = Node(1)
a.next = Node(2)
a.next.next = Node(3)
a.next.next.next = Node(4)
a.next.next.next.next = Node(5)
a.next.next.next.next.next = Node(6)
a.next.next.next.next.next.next = Node(7)
print('list trước khi remove:')
print_list(a)
remove_kth_last(a, 5)
print('list sau khi remove:')
print_list(a)

"""
Độ phức tạp: O(L) với L là độ dài của linked list
"""