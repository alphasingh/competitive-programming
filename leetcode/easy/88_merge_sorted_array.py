"""
https://leetcode.com/problems/merge-sorted-array/
"""


class Solution:
    @staticmethod
    def merge(nums1: [int], m: int, nums2: [int], n: int) -> None:
        pass


assert Solution.merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3) == [1, 2, 2, 3, 5, 6]
assert Solution.merge(nums1=[1], m=1, nums2=[], n=0) == [1]
