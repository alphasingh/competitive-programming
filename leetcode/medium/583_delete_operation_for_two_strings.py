"""
https://leetcode.com/problems/delete-operation-for-two-strings/
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        deletions = 0
        lcs = [word1 + word2]
        print(self, lcs)
        return deletions


solution = Solution()
assert solution.minDistance(word1="sea", word2="eat") == 2
"""
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
"""
assert solution.minDistance(word1="leetcode", word2="etco") == 4
