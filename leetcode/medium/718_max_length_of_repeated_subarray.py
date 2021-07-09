"""
https://leetcode.com/problems/maximum-length-of-repeated-subarray/
"""


class Solution:
    @staticmethod
    def findLength(nums1: [int], nums2: [int]) -> int:
        max_common_length = 0
        nums1_length, nums2_length = len(nums1), len(nums2)
        for start in range(nums1_length):  # traverse nums1
            pointer1 = start
            pointer2 = -1
            current_max = 0
            while (pointer2 < nums2_length - 1) and (pointer1 < nums1_length):
                pointer2 += 1
                # print('p1', pointer1, 'p2', pointer2)
                if nums1[pointer1] == nums2[pointer2]:
                    # print(nums1[pointer1], pointer1, nums2[pointer2], pointer2)
                    current_max += 1
                    pointer1 += 1
                else:
                    pointer1 = start
                    if current_max > 0:
                        pointer2 -= 1
                        current_max = 0
                # max_common_length = max(max_common_length, current_max)
            max_common_length = max(max_common_length, current_max)
        # print(max_common_length)
        return max_common_length


assert Solution.findLength(nums1=[1, 2, 3, 2, 1], nums2=[3, 2, 1, 4, 7]) == 3
# Explanation: The repeated sub array with maximum length is [3,2,1].
assert Solution.findLength(nums1=[0, 0, 0, 0, 0], nums2=[0, 0, 0, 0, 0]) == 5
assert Solution.findLength(nums1=[1, 2, 3, 2, 1], nums2=[3, 2, 1, 4, 7, 1, 2, 3, 2]) == 4
assert Solution.findLength(nums1=[1, 2, 3, 2, 0, 4, 7, 1, 2, 3], nums2=[3, 2, 1, 4, 7, 1, 2, 3, 2]) == 5
