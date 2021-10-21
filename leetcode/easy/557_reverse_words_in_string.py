"""
https://leetcode.com/problems/reverse-words-in-a-string-iii/
"""


class Solution:
    @staticmethod
    def reverseWords(s: str) -> str:
        words = s.split()
        size = len(words)
        for i in range(size):
            words[i] = words[i][::-1]
        return " ".join(words)


assert Solution.reverseWords("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"
assert Solution.reverseWords("God Ding") == "doG gniD"
