"""
https://leetcode.com/problems/count-the-number-of-consistent-strings/
"""


class Solution:
    @staticmethod
    def countConsistentStrings(allowed: str, words: [str]) -> int:
        allowed_set = set(allowed)
        consistent_strings = 0
        for word in words:
            if set(word).issubset(allowed_set):
                consistent_strings += 1
        return consistent_strings


assert Solution.countConsistentStrings(
    allowed="ab", words=["ad", "bd", "aaab", "baa", "badab"]) is 2
assert Solution.countConsistentStrings(
    allowed="abc", words=["a", "b", "c", "ab", "ac", "bc", "abc"]) is 7
assert Solution.countConsistentStrings(
    allowed="cad", words=["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]) is 4

"""
Example 1:
Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
Output: 2
Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.

Example 2:
Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
Output: 7
Explanation: All strings are consistent.

Example 3:
Input: allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
Output: 4
Explanation: Strings "cc", "acd", "ac", and "d" are consistent.
"""
