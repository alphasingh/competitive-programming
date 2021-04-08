"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""


class Solution:

    @staticmethod
    def letterCombinations(digits: str) -> [str]:
        return list(digits)


assert Solution.letterCombinations("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
assert Solution.letterCombinations("") == []
assert Solution.letterCombinations("2") == ["a", "b", "c"]
