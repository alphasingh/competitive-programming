"""
https://leetcode.com/problems/to-lower-case/
"""


class Solution:
    @staticmethod
    def toLowerCase(word: str) -> str:
        return word.lower()


assert Solution.toLowerCase("Hello") == "hello"
assert Solution.toLowerCase("here") == "here"
assert Solution.toLowerCase("LOVELY") == "lovely"
