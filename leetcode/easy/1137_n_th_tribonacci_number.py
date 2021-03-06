"""
https://leetcode.com/problems/n-th-tribonacci-number/
"""


class Solution:
    cache = {}

    def tribonacci_cache(self, n: int) -> int:
        if n == 0:
            return 0
        elif n < 3:
            return 1
        if n not in self.cache:
            tri = self.tribonacci_cache(n - 3) + self.tribonacci_cache(n - 2) + self.tribonacci_cache(n - 1)
            self.cache[n] = tri
        return self.cache[n]

    @staticmethod
    def tribonacci(n: int) -> int:
        a, b, c = 1, 0, 0
        for _ in range(n):
            a, b, c = b, c, a + b + c
        return c


sol = Solution()
assert sol.tribonacci(4) == 4
"""
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
"""
assert sol.tribonacci(25) == 1389537
