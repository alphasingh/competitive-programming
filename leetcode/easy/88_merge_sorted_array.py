"""
https://leetcode.com/problems/merge-sorted-array/
"""


class Solution:
    @staticmethod
    def merge(nums1: [int], m: int, nums2: [int], n: int) -> None:
        i = j = 0
        length_num1 = m + n
        # print(nums1, nums2)
        while i < m and j < n:
            # print(nums1, nums2, 'i', i, 'j', j)
            if nums1[i] > nums2[j]:  # insert nums2[j] at position i in nums1
                for k in range(length_num1 - 1, i, -1):
                    nums1[k], nums1[k - 1] = nums1[k - 1], nums1[k]
                nums1[i] = nums2[j]
                # print(nums1)
                j += 1
                m += 1
            i += 1
        # print(nums1, nums2)
        while j < n:
            # print(nums1, nums2, 'i', i, 'j', j)
            nums1[i] = nums2[j]
            j += 1
            i += 1
        # print(nums1)


input_example = [1, 2, 3, 0, 0, 0]
Solution.merge(nums1=input_example, m=3, nums2=[2, 5, 6], n=3)
assert input_example == [1, 2, 2, 3, 5, 6]

input_example = [1]
Solution.merge(nums1=input_example, m=1, nums2=[], n=0)
assert input_example == [1]

input_example = [1, 2, 6, 8, 0, 0]
Solution.merge(nums1=input_example, m=4, nums2=[3, 7], n=2)
assert input_example == [1, 2, 3, 6, 7, 8]

input_example = [1, 2, 6, 8, 0, 0, 0, 0, 0]
Solution.merge(nums1=input_example, m=4, nums2=[3, 7, 8, 9, 11], n=5)
assert input_example == [1, 2, 3, 6, 7, 8, 8, 9, 11]

input_example = [0]
Solution.merge(nums1=input_example, m=0, nums2=[-1], n=1)
assert input_example == [-1]

input_example = [1, 0]
Solution.merge(nums1=input_example, m=1, nums2=[-1], n=1)
assert input_example == [-1, 1]
