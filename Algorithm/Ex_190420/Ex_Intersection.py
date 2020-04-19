"""
Given two arrays, write a function to compute their intersection -
the intersection means the numbers that are in both arrays
"""


class Solution:

    def intersection(self, nums1, nums2):
        intersection_nums = []
        for i in nums1:
            if i in nums2:
                intersection_nums.append(i)
        return intersection_nums


print(Solution().intersection([4, 9, 5], [9, 4, 9, 8, 4]))
"""
Độ phức tạp: O(n)
"""