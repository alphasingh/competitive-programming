"""
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
"""


class Solution:
    @staticmethod
    def removeDuplicates(s: str) -> str:
        stack = ['a', 'j', 'x']
        s.split()
        result = ''.join(stack)
        print(result)
        return result


assert Solution.removeDuplicates(s="abbaca") == "ca"
"""
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, 
and this is the only possible move.  The result of this move is that the string is "aaca", 
of which only "aa" is possible, so the final string is "ca".
"""
assert Solution.removeDuplicates(s="azxxzy") == "ay"
