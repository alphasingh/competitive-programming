"""
https://leetcode.com/problems/count-vowels-permutation/
"""


class Solution:
    @staticmethod
    def countVowelPermutation(n: int) -> int:
        dp = [[0] * 5 for _ in range(n)]
        dp[0] = [1, 1, 1, 1, 1]
        for i in range(1, n):
            dp[i][0] = dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][4]  # a
            dp[i][1] = dp[i - 1][0] + dp[i - 1][2]  # e
            dp[i][2] = dp[i - 1][1] + dp[i - 1][3]  # i
            dp[i][3] = dp[i - 1][2]  # o
            dp[i][4] = dp[i - 1][2] + dp[i - 1][3]  # u
        return sum(dp[n - 1]) % 1000000007


assert Solution.countVowelPermutation(1) == 5
"""
Explanation: All possible strings are: "a", "e", "i" , "o" and "u".
"""
assert Solution.countVowelPermutation(2) == 10
"""
Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".
"""
assert Solution.countVowelPermutation(5) == 68
