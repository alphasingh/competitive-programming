"""
https://leetcode.com/problems/sort-colors/
"""


class Solution:
    @staticmethod
    def sortColors(nums: [int]) -> None:  # in-place sort
        ends = [0, 0, 0]  # 0, 1, 2
        for num in nums:
            ends[num] += 1
        # print(ends)
        for i in range(len(nums)):
            if i < ends[0]:  # 0
                nums[i] = 0
            elif i < ends[0] + ends[1]:  # 1
                nums[i] = 1
            else:
                nums[i] = 2


numbers = [2, 0, 2, 1, 1, 0]
Solution.sortColors(numbers)
assert numbers == [0, 0, 1, 1, 2, 2]

numbers = [2, 0, 1]
Solution.sortColors(numbers)
assert numbers == [0, 1, 2]

numbers = [0]
Solution.sortColors(numbers)
assert numbers == [0]

numbers = [1]
Solution.sortColors(numbers)
assert numbers == [1]
