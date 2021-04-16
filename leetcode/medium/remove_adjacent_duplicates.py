"""
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
"""


class Solution:

    @staticmethod
    def removeDuplicates(s: str, k: int) -> str:
        # counter = {alphabet: 0 for alphabet in 'abcdefghijklmnopqrstuvwxyz'}
        stack = list()
        for ch in s:
            stack.append(ch)
            last_k = stack[-k:]
            # print(stack, last_k)
            if len(last_k) == k and len(set(last_k)) == 1:
                stack = stack[:-k]
        # print(stack)
        return "".join(stack)


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
