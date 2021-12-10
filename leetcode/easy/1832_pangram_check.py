"""
https://leetcode.com/problems/check-if-the-sentence-is-pangram/
"""


class Solution:
    @staticmethod
    def checkIfPangram(sentence: str) -> bool:
        return len(set(sentence)) == 26


assert Solution.checkIfPangram("thequickbrownfoxjumpsoverthelazydog") is True
assert Solution.checkIfPangram("leetcode") is False
