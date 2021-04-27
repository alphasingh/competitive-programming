"""
https://leetcode.com/problems/4sum-ii/
"""

from itertools import product
from collections import Counter


class Solution:

    @staticmethod
    def fourSumCount(nums1: [int], nums2: [int], nums3: [int], nums4: [int]) -> int:
        n, count = len(nums1), 0
        counter_1x2 = Counter(one + two for one, two in product(nums1, nums2))
        counter_3x4 = Counter(three + four for three, four in product(nums3, nums4))
        for value in counter_1x2:
            if -value in counter_3x4:
                count += counter_1x2[value] * counter_3x4[-value]
        return count


assert Solution.fourSumCount(nums1=[1, 2], nums2=[-2, -1], nums3=[-1, 2], nums4=[0, 2]) == 2
"""
Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0
"""
assert Solution.fourSumCount(nums1=[0], nums2=[0], nums3=[0], nums4=[0]) == 1
