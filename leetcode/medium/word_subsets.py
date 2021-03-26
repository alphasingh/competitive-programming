"""
https://leetcode.com/problems/word-subsets/
"""


class Solution:
    @staticmethod
    def wordSubsets(A: [str], B: [str]) -> [str]:
        return A + B


assert Solution.wordSubsets(A=["amazon", "apple", "facebook", "google", "leetcode"],
                            B=["e", "o"]) == ["facebook", "google", "leetcode"]
assert Solution.wordSubsets(A=["amazon", "apple", "facebook", "google", "leetcode"],
                            B=["l", "e"]) == ["apple", "google", "leetcode"]
assert Solution.wordSubsets(A=["amazon", "apple", "facebook", "google", "leetcode"],
                            B=["e", "oo"]) == ["facebook", "google"]
assert Solution.wordSubsets(A=["amazon", "apple", "facebook", "google", "leetcode"],
                            B=["lo", "eo"]) == ["google", "leetcode"]
assert Solution.wordSubsets(A=["amazon", "apple", "facebook", "google", "leetcode"],
                            B=["ec", "oc", "ceo"]) == ["facebook", "leetcode"]
