"""
https://leetcode.com/problems/minimum-moves-to-equal-array-elements/
"""


class Solution:
    @staticmethod
    def minMoves(nums: [int]) -> int:
        nums.sort(reverse=True)
        moves = 0
        current = nums[0]
        for size, num in enumerate(nums):
            if current != num:
                moves += size * (current - num)
                current = num
        return moves


assert Solution.minMoves([1, 2, 3]) == 3
"""
Explanation: Only three moves are needed (remember each move increments two elements):
[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
"""
assert Solution.minMoves([1, 1, 1]) == 0
assert Solution.minMoves([-7, 2, 8, 4, 1000, 5, 9, -100000000, 100000000]) == 900001021
"""
Some other test cases to confirm the theory
=======================================
INPUT:
=======================================
[1,2,3]
[1,1,1]
[9,9,9,1]
[1]
[-7,2,8,4,5,5,9]
[-7,2,8,4,1000,5,9,-10000]
[-7,2,8,4,1000,5,9,-100000000,100000000]
=======================================
OUTPUT:
=======================================
3
0
24
0
75
71021
900001021
"""
