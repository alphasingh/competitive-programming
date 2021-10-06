"""
https://leetcode.com/problems/find-all-duplicates-in-an-array/
"""


class Solution:

    @staticmethod
    def findDuplicates(nums: [int]) -> [int]:
        length = len(nums)
        iterator = 0  # will increment sequentially
        jumper = 0  # can jump depending on nums[i]

        while iterator < length:
            if nums[jumper] <= length:  # unvisited
                temp = nums[jumper]
                nums[jumper] = length + 1
                if temp <= length:
                    jumper = temp - 1
            else:  # visited
                iterator += 1
                nums[jumper] += 1
                jumper = iterator
        for i in range(length):
            if nums[i] - length == 3:  # 1 extra
                yield i + 1


s = Solution()
assert set(s.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1])) == {2, 3}
assert set(s.findDuplicates([1, 1, 2])) == {1}
assert set(s.findDuplicates([1])) == set()
