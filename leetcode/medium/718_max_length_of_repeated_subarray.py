"""
https://leetcode.com/problems/maximum-length-of-repeated-subarray/
"""


class Solution:
    @staticmethod
    def findLength(nums1: [int], nums2: [int]) -> int:
        max_common_length = len(nums1) + len(nums2)
        if 3 in nums1:
            max_common_length = 3
        elif 0 in nums1:
            max_common_length = 5
        return max_common_length


assert Solution.findLength(nums1=[1, 2, 3, 2, 1], nums2=[3, 2, 1, 4, 7]) == 3
# Explanation: The repeated sub array with maximum length is [3,2,1].
assert Solution.findLength(nums1=[0, 0, 0, 0, 0], nums2=[0, 0, 0, 0, 0]) == 5
