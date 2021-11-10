"""
https://leetcode.com/problems/reverse-prefix-of-word/
"""


class Solution:
    @staticmethod
    def reversePrefix(word: str, ch: str) -> str:
        if ch in word:
            s = word.index(ch)
            return word[0:s + 1][::-1] + word[s + 1:]
        else:
            return word


assert Solution.reversePrefix(word="abcdefd", ch="d") == "dcbaefd"
"""
Explanation: The first occurrence of "d" is at index 3. 
Reverse the part of word from 0 to 3 (inclusive), the resulting string is "dcbaefd".
"""
assert Solution.reversePrefix(word="xyxzxe", ch="z") == "zxyxxe"
"""
Explanation: The first and only occurrence of "z" is at index 3.
Reverse the part of word from 0 to 3 (inclusive), the resulting string is "zxyxxe".
"""
assert Solution.reversePrefix(word="abcd", ch="z") == "abcd"
"""
Explanation: "z" does not exist in word.
You should not do any reverse operation, the resulting string is "abcd".
"""
