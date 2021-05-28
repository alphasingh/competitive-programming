"""
https://leetcode.com/problems/maximum-product-of-word-lengths/
"""


class Solution:
    @staticmethod
    def maxProduct(words: [str]) -> int:
        maximum_product = 0
        alphabets_in_word = [set(word) for word in words]
        length_of_word = [len(word) for word in words]
        # print(alphabets_in_word)
        number_of_words = len(words)
        for i in range(number_of_words):
            for j in range(i + 1, number_of_words):
                if len(alphabets_in_word[i].intersection(alphabets_in_word[j])) == 0:  # empty set
                    current_product = length_of_word[i] * length_of_word[j]
                    maximum_product = max(maximum_product, current_product)
        # print(maximum_product)
        return maximum_product


assert Solution.maxProduct(words=["a", "aa", "aaa", "aaaa"]) == 0
# Explanation: No such pair of words.
assert Solution.maxProduct(words=["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]) == 16
# Explanation: The two words can be "abcw", "xtfn".
assert Solution.maxProduct(words=["a", "ab", "abc", "d", "cd", "bcd", "abcd"]) == 4
# Explanation: The two words can be "ab", "cd".
