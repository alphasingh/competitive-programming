"""
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
"""


class Solution:

    @staticmethod
    def removeDuplicates(s: str, k: int) -> str:
        stack = [["0", 0]]  # character, count
        for character in s:
            if stack[-1][0] == character:  # is on top of stack
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([character, 1])
        return "".join(character * count for character, count in stack)


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
