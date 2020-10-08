"""
704. Binary Search
https://leetcode.com/problems/binary-search/
"""


class Solution:
    @staticmethod
    def search(nums: [int], target: int) -> int:
        for index, num in enumerate(nums):
            if num == target:
                return index
            elif num > target:
                break
        return -1


assert Solution.search(nums=[-1, 0, 3, 5, 9, 12], target=9) == 4
assert Solution.search(nums=[-1, 0, 3, 5, 9, 12], target=2) == -1

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
