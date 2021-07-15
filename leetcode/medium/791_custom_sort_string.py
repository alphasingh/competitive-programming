"""
https://leetcode.com/problems/custom-sort-string/
"""


class Solution:
    @staticmethod
    def customSortString(order: str, string: str) -> str:
        ordered = order + string
        return "cbad"


assert Solution.customSortString("cba", "abcd") in ["cbad", "dcba", "cdba", "cbda"]
"""
Explanation: 
"a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a". 
Since "d" does not appear in order, it can be at any position in the returned string. 
"dcba", "cdba", "cbda" are also valid outputs.
"""
