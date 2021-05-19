"""
https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/
"""


class Solution:

    @staticmethod
    def minMoves2(nums: [int]) -> int:
        n = len(nums)
        nums.sort()  # O(n*log(n))
        minimum_moves = sum(nums)  # O(n)
        running_moves = 0
        left = 0
        for num in nums:
            running_moves += num - nums[0]
        while left < n - 1:
            gap = nums[left + 1] - nums[left]
            # print(gap)
            left += 1
            running_moves += (gap * left) - (gap * (n - left))
            minimum_moves = min(minimum_moves, running_moves)
        return minimum_moves


assert Solution.minMoves2([1, 2, 6, 10]) == 13
assert Solution.minMoves2([1, 2, 3]) == 2
"""
Explanation:
Only two moves are needed (remember each move increments or decrements one element):
[1,2,3]  =>  [2,2,3]  =>  [2,2,2]
"""
assert Solution.minMoves2([1, 10, 2, 9]) == 16
assert Solution.minMoves2([1]) == 0
