"""
https://leetcode.com/problems/split-the-array/
"""


class Solution:
    @staticmethod
    def isPossibleToSplit(nums: [int]) -> bool:
        counter = {}
        for num in nums:
            if num not in counter:
                counter[num] = 0
            counter[num] += 1
            if counter[num] > 2:
                return False
        return True


assert Solution.isPossibleToSplit([1, 0, 1, 0]) == True
assert Solution.isPossibleToSplit([123, 123, 123]) == False
