"""
https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
"""


class Solution:
    @staticmethod
    def smallerNumbersThanCurrent(nums: [int]) -> [int]:
        total = len(nums)
        smaller = [0] * total
        for index in range(total):
            for other in nums:
                if other < nums[index]:
                    smaller[index] += 1
        # print(smaller)
        return smaller


assert Solution.smallerNumbersThanCurrent([8, 1, 2, 2, 3]) == [4, 0, 1, 1, 3]
"""
Explanation: 
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1). 
For nums[3]=2 there exist one smaller number than it (1). 
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
"""
assert Solution.smallerNumbersThanCurrent([6, 5, 4, 8]) == [2, 1, 0, 3]
assert Solution.smallerNumbersThanCurrent([7, 7, 7, 7]) == [0, 0, 0, 0]
