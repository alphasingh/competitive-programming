"""
https://leetcode.com/problems/intersection-of-two-arrays-ii/
"""

from collections import Counter


class Solution:
    @staticmethod
    def intersect(nums1: [int], nums2: [int]) -> [int]:
        intersected = nums1 + nums2
        return intersected


assert Counter(Solution.intersect(nums1=[1, 2, 2, 1], nums2=[2, 2])) == Counter([2, 2])
assert Counter(Solution.intersect(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4])) == Counter([4, 9])
# Explanation: [9,4] is also accepted.
