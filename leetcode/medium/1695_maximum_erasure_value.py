"""
https://leetcode.com/problems/maximum-erasure-value/
"""


class Solution:

    @staticmethod
    def jump(nums: [int]) -> int:
        total_nums = len(nums)
        jumps_needed = [total_nums] * total_nums
        position = jumps_needed[0] = 0  # start
        while position < total_nums:
            position_start = position + 1
            max_position_possible = min(total_nums, position_start + nums[position])
            for current in range(position_start, max_position_possible):
                jumps_needed[current] = min(jumps_needed[current], jumps_needed[position] + 1)
            position += 1
        print(jumps_needed)
        return jumps_needed[-1]


assert Solution.jump(nums=[2, 3, 1, 1, 4]) == 2
"""
Explanation: The minimum number of jumps to reach the last index is 2. 
Jump 1 step from index 0 to 1, then 3 steps to the last index.
"""
assert Solution.jump(nums=[2, 3, 0, 1, 4]) == 2
assert Solution.jump(nums=[9, 0, 0, 0, 0]) == 1
assert Solution.jump(nums=[1, 1, 1, 1, 1]) == 4
assert Solution.jump(nums=[2, 0, 1, 1, 1]) == 3
assert Solution.jump(nums=[2, 0, 2, 1, 1]) == 2
