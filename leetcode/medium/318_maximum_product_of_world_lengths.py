"""
https://leetcode.com/problems/maximum-product-of-word-lengths/
"""


class Solution:
    @staticmethod
    def maxProduct(words: [str]) -> int:
        maximum_product = 0
        return maximum_product


assert Solution.maxProduct(words=["a", "aa", "aaa", "aaaa"]) == 0
# Explanation: No such pair of words.
assert Solution.maxProduct(words=["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]) == 16
# Explanation: The two words can be "abcw", "xtfn".
assert Solution.maxProduct(words=["a", "ab", "abc", "d", "cd", "bcd", "abcd"]) == 4
# Explanation: The two words can be "ab", "cd".
