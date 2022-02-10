"""
https://leetcode.com/problems/rotate-function/
"""


class Solution:
    @staticmethod
    def maxRotateFunction(nums: [int]) -> int:
        m = 0
        n = len(nums)
        r = nums.copy()
        s = 0
        for i in range(n):
            m += i * nums[i]
            r[i] += s
            s = r[i]
        # print(m)
        # print(r)
        s = m
        c = 0
        for i in range(n - 1, 0, -1):
            s = s - ((n - 1) * nums[i]) + (c + r[i - 1])
            c += nums[i]
            m = max(m, s)
            # print(s)
        return m


assert Solution.maxRotateFunction([4, 3, 2, 6]) == 26
"""
Explanation:
F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26
So the maximum value of F(0), F(1), F(2), F(3) is F(3) = 26.
"""
assert Solution.maxRotateFunction([100]) == 0
