"""
https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/
"""


class Solution:
    @staticmethod
    def minStartValue(nums: [int]) -> int:
        running_sum = 0
        msv = 0
        for num in nums:
            running_sum += num
            if running_sum < 0:
                msv = min(msv, running_sum)
        return abs(msv) + 1


assert Solution.minStartValue(nums=[-3, 2, -3, 4, 2]) == 5
"""
Explanation: If you choose startValue = 4, in the third iteration your step by step sum is less than 1.
                step by step sum
                startValue = 4 | startValue = 5 | nums
                  (4 -3 ) = 1  | (5 -3 ) = 2    |  -3
                  (1 +2 ) = 3  | (2 +2 ) = 4    |   2
                  (3 -3 ) = 0  | (4 -3 ) = 1    |  -3
                  (0 +4 ) = 4  | (1 +4 ) = 5    |   4
                  (4 +2 ) = 6  | (5 +2 ) = 7    |   2
"""
assert Solution.minStartValue(nums=[1, 2]) == 1
"""
Explanation: Minimum start value should be positive. 
"""
assert Solution.minStartValue(nums=[1, -2, -3]) == 5
