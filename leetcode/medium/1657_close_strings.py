"""
https://leetcode.com/problems/determine-if-two-strings-are-close/
"""

from collections import Counter


class Solution:
    @staticmethod
    def closeStrings(word1: str, word2: str) -> bool:
        # length should be same
        l1, l2 = len(word1), len(word2)
        # character set should be same
        s1, s2 = set(word1), set(word2)
        # frequency should be same
        f1, f2 = sorted(Counter(word1).values()), sorted(Counter(word2).values())
        return (l1 == l2) and (s1 == s2) and (f1 == f2)


assert Solution.closeStrings(word1="abc", word2="bca") is True
"""
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"
"""
assert Solution.closeStrings(word1="a", word2="aa") is False
"""
Explanation: It is impossible to attain word2 from word1, 
or vice versa, in any number of operations.
"""
assert Solution.closeStrings(word1="cabbba", word2="abbccc") is True
"""
Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"
"""
assert Solution.closeStrings(word1="cabbba", word2="aabbss") is False
"""
Explanation: It is impossible to attain word2 from word1, 
or vice versa, in any amount of operations.
"""
assert Solution.closeStrings(word1="baxxx", word2="babxx") is False
