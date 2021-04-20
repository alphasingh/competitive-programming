"""
https://leetcode.com/problems/unique-paths/
"""


class Solution:
    factorial = [1, 1]

    def fact(self, number: int) -> int:
        if number > len(self.factorial) - 1:
            self.factorial.append(number * self.fact(number - 1))
        return self.factorial[number]

    def uniquePaths(self, m: int, n: int) -> int:
        m, n = m - 1, n - 1
        m, n = max(m, n), min(m, n)
        numerator = 1
        for i in range(m + 1, m + n + 1):
            numerator *= i
        denominator = self.fact(n)
        # print(numerator, denominator)
        unique_paths = numerator // denominator
        # print(self.factorial, unique_paths)
        return unique_paths


sol = Solution()
assert sol.uniquePaths(m=3, n=2) == 3
"""
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
"""
assert sol.uniquePaths(m=3, n=7) == 28
assert sol.uniquePaths(m=7, n=3) == 28
assert sol.uniquePaths(m=3, n=3) == 6
