"""
https://leetcode.com/problems/count-special-quadruplets/
"""


class Solution:
    @staticmethod
    def countQuadruplets(nums: [int]) -> int:
        n = len(nums)
        q = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    for l in range(k + 1, n):
                        if nums[i] + nums[j] + nums[k] == nums[l]:
                            q += 1
        return q


assert Solution.countQuadruplets([1, 2, 3, 6]) == 1
assert Solution.countQuadruplets([3, 3, 6, 4, 5]) == 0
assert Solution.countQuadruplets([1, 1, 1, 3, 5]) == 4
