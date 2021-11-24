"""
https://leetcode.com/problems/buddy-strings/
"""

from collections import Counter


class Solution:
    @staticmethod
    def buddyStrings(s: str, goal: str) -> bool:
        goal_length = len(goal)
        if goal_length != len(s):
            return False
        diff = 0
        for i in range(goal_length):
            if s[i] != goal[i]:
                diff += 1
        if diff == 2 and Counter(goal) == Counter(s):
            return True
        if diff == 0 and len(set(goal)) != goal_length:
            return True
        return False


assert Solution.buddyStrings(s="ab", goal="ba") is True
"""
Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", 
which is equal to goal.
"""
assert Solution.buddyStrings(s="ab", goal="ab") is False
"""
Explanation: The only letters you can swap are s[0] = 'a' and s[1] = 'b', 
which results in "ba" != goal.
"""
assert Solution.buddyStrings(s="aa", goal="aa") is True
"""
Explanation: You can swap s[0] = 'a' and s[1] = 'a' to get "aa", 
which is equal to goal.
"""
assert Solution.buddyStrings(s="aaaaaaabc", goal="aaaaaaacb") is True
assert Solution.buddyStrings(s="abx", goal="xab") is False
assert Solution.buddyStrings(s="abx", goal="a") is False
assert Solution.buddyStrings(s="bat", goal="bed") is False
