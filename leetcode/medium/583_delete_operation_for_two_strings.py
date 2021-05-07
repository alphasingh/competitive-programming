"""
https://leetcode.com/problems/delete-operation-for-two-strings/
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        deletions, word1_size, word2_size = 0, len(word1), len(word2)
        lcs = [[0 for _ in range(word2_size + 1)] for _ in range(word1_size + 1)]
        for i in range(1, word1_size + 1):
            for j in range(1, word2_size + 1):
                if word1[i - 1] == word2[j - 1]:
                    lcs[i][j] = lcs[i - 1][j - 1] + 1
                else:
                    lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])
        return word1_size + word2_size - 2 * lcs[word1_size][word2_size]


solution = Solution()
assert solution.minDistance(word1="sea", word2="eat") == 2
"""
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
"""
assert solution.minDistance(word1="leetcode", word2="etco") == 4
assert solution.minDistance(word1="AGGTAB", word2="GXTXAYB") == 5
