"""
https://leetcode.com/problems/merge-sorted-array/
"""


class Solution:
    @staticmethod
    def merge(nums1: [int], m: int, nums2: [int], n: int) -> None:
        i = j = 0
        while i < m and j < n:
            # print(nums1, nums2, 'i', i, 'j', j)
            if nums1[i] > nums2[j]:  # insert nums2[j] at position i in nums1
                for k in range(m + n - 1, i, -1):
                    nums1[k], nums1[k - 1] = nums1[k - 1], nums1[k]
                nums1[i] = nums2[j]
                j += 1
                m += 1
            i += 1
        while j < n:
            # print(nums1, nums2, 'i', i, 'j', j)
            nums1[i] = nums2[j]
            j += 1
            i += 1
        print(nums1)


input_example = [1, 2, 3, 0, 0, 0]
Solution.merge(nums1=input_example, m=3, nums2=[2, 5, 6], n=3)
assert input_example == [1, 2, 2, 3, 5, 6]

input_example = [1]
Solution.merge(nums1=input_example, m=1, nums2=[], n=0)
assert input_example == [1]
