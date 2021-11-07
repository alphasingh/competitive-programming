"""
https://leetcode.com/problems/keyboard-row/
"""


class Solution:
    @staticmethod
    def findWords(words: [str]) -> [str]:
        valid = []
        rows = (set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm'))
        for word in words:
            creation = set(word.lower())
            if creation.intersection(rows[0]) == creation or creation.intersection(
                    rows[1]) == creation or creation.intersection(rows[2]) == creation:
                valid.append(word)
        return valid


assert Solution.findWords(words=["Hello", "Alaska", "Dad", "Peace"]) == ["Alaska", "Dad"]
assert Solution.findWords(words=["omk"]) == []
assert Solution.findWords(words=["adsdf", "sfd"]) == ["adsdf", "sfd"]
