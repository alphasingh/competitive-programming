"""
https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/
"""


class Solution:

    @staticmethod
    def minMoves2(nums: [int]) -> int:
        return len(nums)


assert Solution.minMoves2([1, 2, 3]) == 2
"""
Explanation:
Only two moves are needed (remember each move increments or decrements one element):
[1,2,3]  =>  [2,2,3]  =>  [2,2,2]
"""
assert Solution.minMoves2([1, 10, 2, 9]) == 16
