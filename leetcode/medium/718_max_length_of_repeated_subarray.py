"""
https://leetcode.com/problems/maximum-length-of-repeated-subarray/
"""


class Solution:
    @staticmethod
    def helper(nums1: [int], nums2: [int]) -> int:
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
                    max_common_length = max(max_common_length, current_max)
                else:
                    pointer1 = start
                    if current_max > 0:
                        pointer2 -= 1
                        current_max = 0
                        max_common_length = max(max_common_length, current_max)
        # print(max_common_length)
        return max_common_length

    @staticmethod
    def findLength_brute(nums1: [int], nums2: [int]) -> int:
        max_common_length = max(Solution.helper(nums1, nums2), Solution.helper(nums2, nums1))
        return max_common_length

    @staticmethod
    def findLength(nums1: [int], nums2: [int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        ans = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = 0
                ans = max(ans, dp[i][j])
        return ans


assert Solution.findLength(nums1=[1, 2, 3, 2, 1], nums2=[3, 2, 1, 4, 7]) == 3
# Explanation: The repeated sub array with maximum length is [3,2,1].
assert Solution.findLength(nums1=[0, 0, 0, 0, 0], nums2=[0, 0, 0, 0, 0]) == 5
assert Solution.findLength(nums1=[1, 2, 3, 2, 1], nums2=[3, 2, 1, 4, 7, 1, 2, 3, 2]) == 4
assert Solution.findLength(nums1=[1, 2, 3, 2, 0, 4, 7, 1, 2, 3], nums2=[3, 2, 1, 4, 7, 1, 2, 3, 2]) == 5
assert Solution.findLength([0, 1, 1, 1, 0], [1, 1, 1, 1, 1]) == 3
assert Solution.findLength([0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]) == 9
