"""
https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/
"""


class Solution:
    @staticmethod
    def isSumEqual(firstWord: str, secondWord: str, targetWord: str) -> bool:
        first_word_value = []
        second_word_value = []
        target_word_value = []
        for char in firstWord:
            value = str(ord(char) - ord('a'))
            first_word_value.append(value)
        first_word_value = "".join(first_word_value)

        for char in secondWord:
            value = str(ord(char) - ord('a'))
            second_word_value.append(value)
        second_word_value = "".join(second_word_value)

        for char in targetWord:
            value = str(ord(char) - ord('a'))
            target_word_value.append(value)
        target_word_value = "".join(target_word_value)

        # print(first_word_value, second_word_value, target_word_value)
        return int(first_word_value) + int(second_word_value) == int(target_word_value)


assert Solution.isSumEqual(firstWord="acb", secondWord="cba", targetWord="cdb") is True
"""
Explanation:
The numerical value of firstWord is "acb" -> "021" -> 21.
The numerical value of secondWord is "cba" -> "210" -> 210.
The numerical value of targetWord is "cdb" -> "231" -> 231.
We return true because 21 + 210 == 231.
"""
assert Solution.isSumEqual(firstWord="aaa", secondWord="a", targetWord="aab") is False
"""
Explanation: 
The numerical value of firstWord is "aaa" -> "000" -> 0.
The numerical value of secondWord is "a" -> "0" -> 0.
The numerical value of targetWord is "aab" -> "001" -> 1.
We return false because 0 + 0 != 1.
"""
assert Solution.isSumEqual(firstWord="aaa", secondWord="a", targetWord="aaaa") is True
"""
Explanation: 
The numerical value of firstWord is "aaa" -> "000" -> 0.
The numerical value of secondWord is "a" -> "0" -> 0.
The numerical value of targetWord is "aaaa" -> "0000" -> 0.
We return true because 0 + 0 == 0.
"""
