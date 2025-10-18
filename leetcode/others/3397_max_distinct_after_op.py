"""
https://leetcode.com/problems/maximum-number-of-distinct-elements-after-operations/
3397. Maximum Number of Distinct Elements After Operations
"""
from cmath import inf
from typing import List


class Solution:
    @staticmethod
    def maxDistinctElements(nums: List[int], k: int) -> int:
        nums.sort()
        next_avail = -inf
        count = 0
        for num in nums:
            if num - k >= next_avail:
                next_avail = num - k + 1
                count += 1
            elif num - k < next_avail <= num + k:
                next_avail += 1
                count += 1
        return count


assert Solution.maxDistinctElements([1,2,2,3,3,4], 2) == 6
assert Solution.maxDistinctElements([4,4,4,4], 1) == 3
assert Solution.maxDistinctElements([1,1,1,1,1,1,1,1,5,5,5], 3) == 10
assert Solution.maxDistinctElements([8,8,10,9,9], 1) == 5
assert Solution.maxDistinctElements([7,8,10,10,7,6,7], 1) == 7