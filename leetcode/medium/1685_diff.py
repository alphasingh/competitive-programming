"""
https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/
"""


class Solution:
    @staticmethod
    def getSumAbsoluteDifferences(nums: [int]) -> [int]:
        n = len(nums)
        left = right = 0

        for i in range(n):
            right += (nums[i] - nums[0])

        # print(left, right)
        d = [right]
        for i in range(1, n):
            diff = nums[i] - nums[i - 1]
            left -= diff * i
            right -= diff * (n - i)
            # print(left, right)
            d.append(right - left)
        """
        [1,4,6,8,10]
        [0,3,5,7,9]     24
        [-3,0,2,4,6]    15
        [-5,-2,0,2,4]   13
        [-7,-4,-2,0,2]  15
        [-9,-6,-4,-2,0] 21

        sliding window
        abs(negatives) + positives

        1. calculate difference of first element with every element
        2. store the sum as running sum (left=0 and right=sum)
        3. we will keep moving to right and update left and right
        4. all_left * diff will be subtracted from left
        5. all_right * diff will be added to right
        6. keep updating till reach end

        """

        return d


assert Solution.getSumAbsoluteDifferences([2, 3, 5]) == [4, 3, 5]
"""
Explanation: Assuming the arrays are 0-indexed, then
result[0] = |2-2| + |2-3| + |2-5| = 0 + 1 + 3 = 4,
result[1] = |3-2| + |3-3| + |3-5| = 1 + 0 + 2 = 3,
result[2] = |5-2| + |5-3| + |5-5| = 3 + 2 + 0 = 5.
"""
assert Solution.getSumAbsoluteDifferences([1, 4, 6, 8, 10]) == [24, 15, 13, 15, 21]
