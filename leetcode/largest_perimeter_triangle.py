"""
https://leetcode.com/problems/largest-perimeter-triangle/
"""


class Solution:
    @staticmethod
    def largestPerimeter(nums: [int]) -> int:
        largest_perimeter = 0
        nums.sort(reverse=True)
        for i in range(len(nums) - 2):  # all possible triplets
            if nums[i] < nums[i + 1] + nums[i + 2]:  # basic triangle property
                largest_perimeter = nums[i] + nums[i + 1] + nums[i + 2]
                break
        return largest_perimeter


assert Solution.largestPerimeter(nums=[2, 1, 2]) == 5
assert Solution.largestPerimeter(nums=[1, 2, 1]) == 0
assert Solution.largestPerimeter(nums=[3, 2, 3, 4]) == 10
assert Solution.largestPerimeter(nums=[3, 6, 2, 3]) == 8

"""
Example 1:
Input: nums = [2,1,2]
Output: 5

Example 2:
Input: nums = [1,2,1]
Output: 0

Example 3:
Input: nums = [3,2,3,4]
Output: 10

Example 4:
Input: nums = [3,6,2,3]
Output: 8
"""
