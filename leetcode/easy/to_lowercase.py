"""
https://leetcode.com/problems/to-lower-case/
"""


class Solution:
    @staticmethod
    def toLowerCase(word: str) -> str:
        lower = list(word)
        for index, character in enumerate(word):
            ordinal_character = ord(character)
            if 65 <= ordinal_character <= 90:
                lower[index] = chr(ordinal_character + 32)
        return "".join(lower)


assert Solution.toLowerCase("Hello") == "hello"
assert Solution.toLowerCase("here") == "here"
assert Solution.toLowerCase("LOVELY") == "lovely"
