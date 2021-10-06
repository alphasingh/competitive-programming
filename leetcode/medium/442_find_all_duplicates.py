"""
https://leetcode.com/problems/find-all-duplicates-in-an-array/
"""


class Solution:

    def findDuplicates(self, nums: [int]) -> [int]:
        length = len(nums)
        # print(nums)
        pointer = 0
        _i = 0

        while pointer < length:
            if nums[_i] <= length:  # unvisited
                temp = nums[_i]
                nums[_i] = length + 1
                if temp <= length:
                    _i = temp - 1
            else:  # visited
                pointer += 1
                nums[_i] += 1
                _i = pointer
            # index = nums[_i] % 7 - 1
            # if nums[index] <= length:
            #     nums[index] = length
            # nums[index] += 1
            #
            # self.pointer += 1

        # while pointer < length:
        #     update(pointer)
        #     ahead = nums[pointer]
        #     update(ahead)
        #     pointer += 1

        # print(nums)
        # indices = set()
        for i in range(length):
            if nums[i] - length == 3:  # 1 extra
                yield i + 1


s = Solution()
assert set(s.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1])) == {2, 3}
assert set(s.findDuplicates([1, 1, 2])) == {1}
assert set(s.findDuplicates([1])) == set()
