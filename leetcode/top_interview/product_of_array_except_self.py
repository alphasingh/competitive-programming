"""
https://leetcode.com/problems/battleships-in-a-board/
"""


class Solution:
    @staticmethod
    def productExceptSelf(nums: [int]) -> [int]:
        product = 1
        pivot = 0
        if nums.count(0) > 0:
            pivot = nums.index(0)
        for i in range(len(nums)):
            if i != pivot:
                product *= nums[i]
        # print(product, pivot)
        product_with_pivot = product * nums[pivot]
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = product
            else:
                nums[i] = product_with_pivot // nums[i]
        # print(nums)
        return nums


assert Solution.productExceptSelf(nums=[1, 2, 3, 4]) == [24, 12, 8, 6]
assert Solution.productExceptSelf(nums=[-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
