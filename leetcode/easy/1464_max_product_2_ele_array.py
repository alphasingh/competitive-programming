"""
https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/
"""


class Solution:
    @staticmethod
    def maxProduct(nums: [int]) -> int:
        nums.sort()
        # print(nums)
        return (nums[-1] - 1) * (nums[-2] - 1)


assert Solution.maxProduct(nums=[3, 4, 5, 2]) == 12
"""
Explanation: If you choose the indices i=1 and j=2 (indexed from 0), 
you will get the maximum value, 
that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12. 
"""
assert Solution.maxProduct(nums=[1, 5, 4, 5]) == 16
"""
Explanation: Choosing the indices i=1 and j=3 (indexed from 0), 
you will get the maximum value of (5-1)*(5-1) = 16.
"""
assert Solution.maxProduct(nums=[3, 7]) == 12
