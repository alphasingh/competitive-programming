"""
https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations
"""
from collections import Counter
from typing import List

class Solution:
    @staticmethod
    def findSmallestInteger(nums: List[int], value: int) -> int:
        used = set()
        # print(f"nums:{nums}")
        for i, num in enumerate(nums):
            after = num % value
            # print(f"numBefore:{num};numAfter:{after};")
            nums[i] = after
        counter = Counter(nums)
        # print(f"counter:{counter}")
        for num, count in counter.items():
            for times in range(count):
                used.add(num + times * value)
        # print(f"used:{used}")
        # print(f"nums:{nums}")
        nums = sorted(used)
        # print(f"nums:{nums}")
        MEX = nums[-1] + 1
        for i, num in enumerate(nums):
            if num != i:
                return i
        return MEX

"""
nums = [1,-10,7,13,6,8], value = 5


BEST CASE:
value is minimum -> MEX will be max possible
nums = [0,1,2,3,4,5], value = 1 
MEX will be 6 since with value 1 
as we can do any possible operation on any number


WORST CASE:
if value is high -> low MEX is possible
nums = [1,-10,7,13,6,8], value = 10
nums = [1,-10,7,13,6,8], value = 10

IDEA:
what if we modulus all numbers with value
we can get sequence, which we can start offset with 0
from there we can find maximum MEX possible

we can reuse some mod values if they are not already used
best way to reuse is to use them in increasing order

nums = [1,-10,7,13,6,8], value = 10
"""


sol = Solution()
assert sol.findSmallestInteger([1,-10,7,13,6,8], 5) == 4
assert sol.findSmallestInteger([1,-10,7,13,6,8], 7) == 2
assert sol.findSmallestInteger([1,-10,7,13,6,8], 10) == 2
assert sol.findSmallestInteger([1,-10,7,13,6,8], 1000) == 0
assert sol.findSmallestInteger([1000001,-10,72029191,13,600000000,-10202098], 1008) == 0
assert sol.findSmallestInteger([3,0,3,2,4,2,1,1,0,4], 5) == 10
assert sol.findSmallestInteger([0,0,0,0,1,0,0,1,0,0,1,1,0,1,0,1,1], 2) == 15