"""
https://leetcode.com/problems/range-sum-query-immutable/
"""


class NumArray:

    def __init__(self, nums: [int]):
        self.running_sums = nums.copy()
        for i in range(1, len(nums)):
            self.running_sums[i] += self.running_sums[i - 1]

    def sumRange(self, left: int, right: int) -> int:
        return self.running_sums[right] - (self.running_sums[left - 1] if left else 0)


numArray = NumArray([-2, 0, 3, -5, 2, -1])
assert numArray.sumRange(0, 2) == 1  # return (-2) + 0 + 3 = 1
assert numArray.sumRange(2, 5) == -1  # return 3 + (-5) + 2 + (-1) = -1
assert numArray.sumRange(0, 5) == -3  # return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3
