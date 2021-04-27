"""
https://leetcode.com/problems/4sum-ii/
"""


class Solution:

    @staticmethod
    def fourSumCount(nums1: [int], nums2: [int], nums3: [int], nums4: [int]) -> int:
        n = len(nums1)
        count = n + len(nums2) + len(nums3) + len(nums4)
        return count


assert Solution.fourSumCount(nums1=[1, 2], nums2=[-2, -1], nums3=[-1, 2], nums4=[0, 2]) == 2
"""
Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0
"""
assert Solution.fourSumCount(nums1=[0], nums2=[0], nums3=[0], nums4=[0]) == 1
