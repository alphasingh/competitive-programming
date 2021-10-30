"""
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
"""


class Solution:
    @staticmethod
    def findDisappearedNumbers(nums: [int]) -> [int]:
        disappeared = []
        n = len(nums)
        for i in range(n):
            index = (nums[i] - 1) % n
            nums[index] += n
            # print(nums)
        for i in range(n):
            if nums[i] <= n:
                disappeared.append(i + 1)
        return disappeared


assert Solution.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6]
assert Solution.findDisappearedNumbers([1, 1]) == [2]
