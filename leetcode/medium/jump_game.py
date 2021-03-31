"""
https://leetcode.com/problems/jump-game/
"""


class Solution:
    @staticmethod
    def canJump(nums: [int]) -> bool:
        return len(nums) ^ 1 == 0


assert Solution.canJump(nums=[2, 3, 1, 1, 4]) is True
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
assert Solution.canJump(nums=[3, 2, 1, 0, 4]) is False
# Explanation: You will always arrive at index 3 no matter what.
# Its maximum jump length is 0, which makes it impossible to reach the last index.
