"""
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
"""


class Solution:

    @staticmethod
    def removeDuplicates(s: str, k: int) -> str:
        result = s
        removal_start = 0
        # print("k:", k)
        length_of_result = len(result)
        while removal_start <= length_of_result - k:
            to_be_removed = result[removal_start:removal_start + k]
            # print(result, length_of_result, to_be_removed)
            if len(to_be_removed) == k and len(set(to_be_removed)) == 1:  # k adjacent duplicates
                length_of_result -= k
                result = result[:removal_start] + result[removal_start + k:]
                removal_start = 0
            else:
                removal_start += 1
        return result


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
