"""
https://leetcode.com/problems/three-consecutive-odds/
"""


class Solution:
    @staticmethod
    def threeConsecutiveOdds(arr: [int]) -> bool:
        n = len(arr)
        for i in range(n - 2):
            if arr[i] % 2 != 0 and arr[i + 1] % 2 != 0 and arr[i + 2] % 2 != 0:
                return True
        return False


assert Solution.threeConsecutiveOdds(arr=[2, 6, 4, 1]) is False
assert Solution.threeConsecutiveOdds(arr=[1, 2, 34, 3, 4, 5, 7, 23, 12]) is True
# Explanation: [5,7,23] are three consecutive odds.
