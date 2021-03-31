"""
https://leetcode.com/problems/jump-game/
"""


class Solution:
    @staticmethod
    def canJump(nums: [int]) -> bool:
        to_be_visited = [0]  # first visit at the starting index
        size_nums = len(nums)
        visited = [False] * size_nums  # to keep track of the visited elements
        max_visit = 0  # maximum visit reached
        while to_be_visited:
            current_visit = to_be_visited.pop()
            visited[current_visit] = True
            range_start = current_visit + 1
            range_end = range_start + nums[current_visit]  # until maximum jump
            if range_end >= size_nums:
                visited[-1] = True  # last index can be reached
                break
            if range_end <= max_visit:
                continue
            else:
                range_start = max_visit
            for index in range(range_start, range_end):
                if not visited[index] and index not in to_be_visited:
                    to_be_visited.append(index)
        return visited[-1]  # last index visited


assert Solution.canJump(nums=[2, 3, 1, 1, 4]) is True
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
assert Solution.canJump(nums=[3, 2, 1, 0, 4]) is False
# Explanation: You will always arrive at index 3 no matter what.
# Its maximum jump length is 0, which makes it impossible to reach the last index.
