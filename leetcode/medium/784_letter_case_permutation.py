"""
https://leetcode.com/problems/letter-case-permutation/
"""


class Solution:
    @staticmethod
    def letterCasePermutation(s: str) -> [str]:
        p = set()
        n = len(s)

        def dfs(i, c):  # starting from index i
            if i >= n:
                p.add(c)
                return c
            dfs(i + 1, c + s[i].upper())
            dfs(i + 1, c + s[i].lower())

        dfs(0, '')  # start from 0 with empty string
        return p


assert Solution.letterCasePermutation("a1b2") == {"a1b2", "a1B2", "A1b2", "A1B2"}
assert Solution.letterCasePermutation("3z4") == {"3z4", "3Z4"}
