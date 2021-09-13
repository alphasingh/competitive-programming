"""
https://leetcode.com/problems/intersection-of-two-arrays-ii/
"""

from collections import Counter


class Solution:
    @staticmethod
    def intersect(nums1: [int], nums2: [int]) -> [int]:
        intersected = []
        nc1 = Counter(nums1)
        nc2 = Counter(nums2)
        for key in nc1:
            if key in nc2:
                intersected += [key] * min(nc1[key], nc2[key])
        # print(intersected)
        return intersected


assert Counter(Solution.intersect(nums1=[1, 2, 2, 1], nums2=[2, 2])) == Counter([2, 2])
assert Counter(Solution.intersect(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4])) == Counter([4, 9])
# Explanation: [9,4] is also accepted.
