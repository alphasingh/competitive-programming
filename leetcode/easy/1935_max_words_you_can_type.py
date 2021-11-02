"""
https://leetcode.com/problems/maximum-number-of-words-you-can-type/
"""


class Solution:
    @staticmethod
    def canBeTypedWords(text: str, brokenLetters: str) -> int:
        words = text.split()
        can_be_typed = 0
        broken_letters = set(brokenLetters)
        for word in words:
            if len(set(word).intersection(set(broken_letters))) == 0:
                can_be_typed += 1
        return can_be_typed


assert Solution.canBeTypedWords(text="hello world", brokenLetters="ad") == 1
# Explanation: We cannot type "world" because the 'd' key is broken.
assert Solution.canBeTypedWords(text="leet code", brokenLetters="lt") == 1
# Explanation: We cannot type "leet" because the 'l' and 't' keys are broken.
assert Solution.canBeTypedWords(text="leet code", brokenLetters="e") == 0
# Explanation: We cannot type either word because the 'e' key is broken.
