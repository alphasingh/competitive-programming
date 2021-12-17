"""
https://leetcode.com/problems/merge-strings-alternately/
"""


class Solution:
    @staticmethod
    def mergeAlternately(word1: str, word2: str) -> str:
        pointer1 = pointer2 = 0
        size1 = len(word1)
        size2 = len(word2)
        merged = ""
        while pointer1 < size1 or pointer2 < size2:
            if pointer1 < size1:
                merged += word1[pointer1]
                pointer1 += 1
            if pointer2 < size2:
                merged += word2[pointer2]
                pointer2 += 1
        return merged


assert Solution.mergeAlternately(word1="abc", word2="pqr") == "apbqcr"
"""
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
"""
assert Solution.mergeAlternately(word1="ab", word2="pqrs") == "apbqrs"
"""
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
"""
assert Solution.mergeAlternately(word1="abcd", word2="pq") == "apbqcd"
"""
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
"""
