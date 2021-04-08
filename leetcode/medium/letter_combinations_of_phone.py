"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""


class Solution:
    KEYS = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

    @staticmethod
    def letterCombinations(digits: str) -> [str]:
        combinations = []
        return combinations


assert Solution.letterCombinations("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
assert Solution.letterCombinations("") == []
assert Solution.letterCombinations("2") == ["a", "b", "c"]
