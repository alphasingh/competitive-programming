"""
https://leetcode.com/problems/single-element-in-a-sorted-array/
"""


class Solution:
    @staticmethod
    def singleNonDuplicate(nums: [int]) -> int:
        L = 0
        SIZE = len(nums)
        R = SIZE - 1
        while L <= R:
            M = (L + R) // 2
            if M % 2 == 0:  # even index
                # go in direction of duplicate
                if M > 0 and nums[M - 1] == nums[M]:  # check left
                    R = M - 1
                elif M < SIZE - 1 and nums[M + 1] == nums[M]:  # check right
                    L = M + 1
                else:
                    return nums[M]
            else:  # odd index
                # go opp to direction of duplicate
                if M > 0 and nums[M - 1] == nums[M]:  # check left
                    L = M + 1
                elif M < SIZE - 1 and nums[M + 1] == nums[M]:  # check right
                    R = M - 1
                else:
                    return nums[M]
        return -1


assert Solution.singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]) == 2
assert Solution.singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]) == 10
