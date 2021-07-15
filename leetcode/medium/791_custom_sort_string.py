"""
https://leetcode.com/problems/custom-sort-string/
"""


class Solution:
    ALPHABETS = 'abcdefghijklmnopqrstuvwxyz'

    def customSortString(self, order: str, string: str) -> str:
        ordered = ''
        string_counter = {alphabet: 0 for alphabet in self.ALPHABETS}
        for ch in string:
            string_counter[ch] += 1
        string_set = set(string)
        order_set = set(order)
        # print(order_set, string_set)
        string_set_not_in_order_set = string_set.difference(order_set)
        # print(string_set_not_in_order_set)
        # print(string_counter)
        ordered += ''.join([alphabet * string_counter[alphabet] for alphabet in order])
        ordered += ''.join([alphabet * string_counter[alphabet] for alphabet in string_set_not_in_order_set])
        # print(ordered)
        return ordered


sol = Solution()
assert sol.customSortString("cba", "abcd") in ["cbad", "dcba", "cdba", "cbda"]
"""
Explanation: 
"a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a". 
Since "d" does not appear in order, it can be at any position in the returned string. 
"dcba", "cdba", "cbda" are also valid outputs.
"""
