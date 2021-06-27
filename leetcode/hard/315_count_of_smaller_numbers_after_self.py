"""
https://leetcode.com/problems/count-of-smaller-numbers-after-self/
"""


class Solution:
    @staticmethod
    def countSmaller(nums: [int]) -> [int]:
        smaller = nums.copy()
        return smaller


assert Solution.countSmaller(nums=[5, 2, 6, 1]) == [2, 1, 1, 0]
"""
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
"""
assert Solution.countSmaller(nums=[-1]) == [0]
assert Solution.countSmaller(nums=[-1, -1]) == [0, 0]
