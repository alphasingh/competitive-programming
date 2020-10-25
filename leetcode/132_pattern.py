"""
https://leetcode.com/problems/132-pattern/
"""


class Solution:
    @staticmethod
    def find132pattern(nums: [int]) -> bool:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] < nums[k] < nums[j]:
                        return True
        return False


assert Solution.find132pattern(nums=[1, 2, 3, 4]) is False
assert Solution.find132pattern(nums=[-1, 3, 2, 0]) is True
assert Solution.find132pattern(nums=[3, 1, 4, 2]) is True
"""
Input: nums = [1,2,3,4]
Output: false
Explanation: There is no 132 pattern in the sequence.

Input: nums = [3,1,4,2]
Output: true
Explanation: There is a 132 pattern in the sequence: [1, 4, 2].

Input: nums = [-1,3,2,0]
Output: true
Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
"""
