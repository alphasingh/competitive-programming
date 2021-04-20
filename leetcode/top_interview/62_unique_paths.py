"""
https://leetcode.com/problems/unique-paths/
"""


class Solution:

    @staticmethod
    def uniquePaths(m: int, n: int) -> int:
        unique_paths = 1
        return unique_paths


assert Solution.uniquePaths(m=3, n=2) == 3
"""
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
"""
assert Solution.uniquePaths(m=3, n=7) == 28
assert Solution.uniquePaths(m=7, n=3) == 28
assert Solution.uniquePaths(m=3, n=3) == 6
