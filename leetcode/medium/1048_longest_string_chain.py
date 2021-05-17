"""
https://leetcode.com/problems/longest-string-chain/
"""


class Solution:

    def longestStrChain(self, words: [str]) -> int:
        def dfs(memo, word):
            if word in memo:
                return memo[word]
            max_length = 1
            for i in range(len(word)):
                new_word = word[:i] + word[i + 1:]
                # print(word, newWord)
                if new_word in words_present:
                    new_word_length = 1 + dfs(memo, new_word)
                    max_length = max(max_length, new_word_length)
            memo[word] = max_length
            return max_length

        words_present = set(words)
        memo = {}
        answer = 0
        for word in words:
            answer = max(answer, dfs(memo, word))
        return answer


sol = Solution()
assert sol.longestStrChain(["a", "b", "ba", "bca", "bda", "bdca"]) == 4
# Explanation: One of the longest word chain is "a","ba","bda","bdca".
assert sol.longestStrChain(["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]) == 5
