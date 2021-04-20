"""
https://leetcode.com/problems/find-the-duplicate-number/
"""


class Solution:

    @staticmethod
    def findDuplicate(nums: [int]) -> int:
        counter = [0 for _ in nums]
        for num in nums:
            counter[num - 1] += 1
        # print(counter)
        duplicate = 1
        for num in nums:
            if counter[num - 1] > 1:
                duplicate = num
                break
        return duplicate


sol = Solution()

assert sol.findDuplicate(nums=[1, 3, 4, 2, 2]) == 2
assert sol.findDuplicate(nums=[3, 1, 3, 4, 2]) == 3
assert sol.findDuplicate(nums=[1, 1]) == 1
assert sol.findDuplicate(nums=[1, 1, 2]) == 1
assert sol.findDuplicate(nums=[2, 2, 2]) == 2
assert sol.findDuplicate(nums=[1, 3, 4, 4, 4]) == 4
