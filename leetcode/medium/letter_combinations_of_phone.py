"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""


class Solution:
    KEYS = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

    @staticmethod
    def letterCombinations(digits: str) -> [str]:
        combinations = []
        for digit in digits:
            if len(combinations) == 0:
                combinations = list(Solution.KEYS[digit])
            else:
                current_combinations = []
                for combination in combinations:
                    for letter in Solution.KEYS[digit]:
                        current_combinations.append(combination + letter)
                combinations = current_combinations.copy()
        # print(combinations)
        return combinations


assert Solution.letterCombinations("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
assert Solution.letterCombinations("") == []
assert Solution.letterCombinations("2") == ["a", "b", "c"]
assert Solution.letterCombinations("78") == ["pt", "pu", "pv", "qt", "qu", "qv", "rt", "ru", "rv", "st", "su", "sv"]
