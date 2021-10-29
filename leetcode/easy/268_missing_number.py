"""
https://leetcode.com/problems/missing-number/
"""


class Solution:
    @staticmethod
    def missingNumber(nums: [int]) -> int:
        s = sum(nums)
        n = len(nums)
        sn = n * (n + 1) // 2
        # print(sn)
        return sn - s


assert Solution.missingNumber([3, 0, 1]) == 2
"""
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 
2 is the missing number in the range since it does not appear in nums.
"""

assert Solution.missingNumber([0, 1]) == 2
"""
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 
2 is the missing number in the range since it does not appear in nums.
"""
assert Solution.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
"""
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 
8 is the missing number in the range since it does not appear in nums.
"""
assert Solution.missingNumber([0]) == 1
"""
Explanation: n = 1 since there is 1 number, so all numbers are in the range [0,1]. 
1 is the missing number in the range since it does not appear in nums.
"""
