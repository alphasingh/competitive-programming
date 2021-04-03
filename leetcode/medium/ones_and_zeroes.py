"""
https://leetcode.com/problems/ones-and-zeroes/
"""


class Solution:

    @staticmethod
    def findMaxForm(binaries: [str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for binary in binaries:
            z, o = binary.count('0'), binary.count('1')
            for x in range(m, z - 1, -1):
                for y in range(n, o - 1, -1):
                    dp[x][y] = max(1 + dp[x - z][y - o], dp[x][y])
        return dp[m][n]


assert Solution.findMaxForm(binaries=["10", "0001", "111001", "1", "0"], m=5, n=3) == 4
"""
Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
{"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.
"""
assert Solution.findMaxForm(binaries=["10", "0", "1"], m=1, n=1) == 2
"""
The largest subset is {"0", "1"}, so the answer is 2.
"""
