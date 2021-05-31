"""
https://leetcode.com/problems/maximum-gap/
"""


class Solution:

    @staticmethod
    def maximumGap(nums: [int]) -> int:
        maximum_gap = 0
        return maximum_gap


assert Solution.maximumGap([3, 6, 9, 1]) == 3
# Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.
assert Solution.maximumGap([10]) == 0
# Explanation: The array contains less than 2 elements, therefore return 0.
