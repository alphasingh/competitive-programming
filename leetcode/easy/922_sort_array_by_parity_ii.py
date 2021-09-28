"""
https://leetcode.com/problems/sort-array-by-parity-ii/
"""


class Solution:
    @staticmethod
    def sortArrayByParityII(nums: [int]) -> [int]:
        parity = nums.copy()
        even = 0
        odd = 1
        for num in nums:
            if num % 2 == 0:  # even index
                parity[even] = num
                even += 2
            else:
                parity[odd] = num
                odd += 2
        return parity


assert Solution.sortArrayByParityII(nums=[4, 2, 5, 7]) in [[4, 5, 2, 7],
                                                           [4, 7, 2, 5],
                                                           [2, 5, 4, 7],
                                                           [2, 7, 4, 5]]
assert Solution.sortArrayByParityII(nums=[2, 3]) in [[2, 3]]
