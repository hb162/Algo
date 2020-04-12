"""
Given an array, nums, of n integers, find all unique triplets (three numbers, a, b, c) in nums such that a + b + c = 0.
Note that there may not be any triplets that sum to zero in nums, and that the triplets must not be dupicates
"""


class Solution:
    def threeSum(self, nums):
        nums.sort()
        found = False
        n = len(nums)
        for i in range(n):
            left = i + 1
            right = n - 1
            x = nums[i]
            while left < right:
                sum = x + nums[left] + nums[right]
                if sum == 0:
                    print([x, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    found = True
                elif sum < 0:
                    left += 1
                else:
                    right -= 1
        if found == False:
            print("None")


list = [1, -2, 1, 0, 5]
Solution().threeSum(list)
