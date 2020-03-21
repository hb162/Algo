"""
Given a list, find the k-th largest element in the list
"""


list = [-9, 91, 5, 0, 8, 10]


def heapify(list, n, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and list[i] > list[left]:
        smallest = left
    if right < n and list[right] < list[smallest]:
        smallest = right
    if smallest != i:
        list[i], list[smallest] = list[smallest], list[i]
        heapify(list, n, smallest)


def min_heap(list, n):
    for i in range(n//2 -1, -1, -1):
        heapify(list, n, i)


def kth_largest(list, n, k):
    min = [0] * k
    for i in range(0, k):
        min[i] = list[i]
    min_heap(min, k)
    for i in range(k, n):
        if list[i] > min[0]:
            min[0] = list[i]
            heapify(min, k, 0)
    return min[0]


print(kth_largest(list, len(list), 4))
"""
Độ phức tạp: O(
"""