"""
https://leetcode.com/problems/longest-string-chain/
"""


class Solution:

    def longestStrChain(self, words: [str]) -> int:
        return len(words)


sol = Solution()
assert sol.longestStrChain(["a", "b", "ba", "bca", "bda", "bdca"]) == 4
# Explanation: One of the longest word chain is "a","ba","bda","bdca".
assert sol.longestStrChain(["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]) == 5
