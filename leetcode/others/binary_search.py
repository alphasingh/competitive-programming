"""
704. Binary Search
https://leetcode.com/problems/binary-search/
"""

from bisect import bisect_left


class Solution:
    @staticmethod
    def search(nums: [int], target: int) -> int:
        index = bisect_left(nums, target)
        if target > nums[-1] or target < nums[0] or nums[index] != target:
            index = -1
        return index


assert Solution.search(nums=[-1, 0, 3, 5, 9, 12], target=9) == 4
assert Solution.search(nums=[-1, 0, 3, 5, 9, 12], target=2) == -1
assert Solution.search(nums=[-1, 0, 3, 5, 9, 12], target=14) == -1

"""
Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
"""
