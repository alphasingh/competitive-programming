"""
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
"""


class Solution:

    @staticmethod
    def removeDuplicates(s: str, k: int) -> str:
        return s + str(k)


assert Solution.removeDuplicates(s="abcd", k=2) == "abcd"
"""Explanation: There's nothing to delete."""
assert Solution.removeDuplicates(s="deeedbbcccbdaa", k=3) == "aa"
"""
Explanation: 
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"
"""
assert Solution.removeDuplicates(s="pbbcggttciiippooaais", k=2) == "ps"
