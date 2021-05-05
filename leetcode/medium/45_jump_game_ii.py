"""
https://leetcode.com/problems/jump-game-ii/
"""


class Solution:

    @staticmethod
    def jump(nums: [int]) -> int:
        total_nums = len(nums)
        jumps_needed = [0] * total_nums
        position = 0  # start
        while position < total_nums:
            position += 1
        return jumps_needed[-1]


assert Solution.jump(nums=[2, 3, 1, 1, 4]) == 2
"""
Explanation: The minimum number of jumps to reach the last index is 2. 
Jump 1 step from index 0 to 1, then 3 steps to the last index.
"""
assert Solution.jump(nums=[2, 3, 0, 1, 4]) == 2
