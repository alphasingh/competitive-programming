"""
https://leetcode.com/problems/get-equal-substrings-within-budget/
"""


class Solution:
    @staticmethod
    def equalSubstring(s: str, t: str, maxCost: int) -> int:
        start = equal = 0
        length = len(s)  # same as len(t)
        costs = [0] * length  # costs required to make s[i] to t[i]
        for i in range(length):
            costs[i] = abs(ord(s[i]) - ord(t[i]))
        # print(costs)
        current = 0
        for end in range(length):
            current += costs[end]
            while current > maxCost:
                current -= costs[start]
                start += 1
            equal = max(equal, end - start + 1)
        # print(equal)
        return equal


assert Solution.equalSubstring("abcd", "bcdf", 3) == 3
assert Solution.equalSubstring("abcd", "cdef", 3) == 1
assert Solution.equalSubstring("abcd", "acde", 0) == 1
