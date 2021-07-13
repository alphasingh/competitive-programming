"""
https://leetcode.com/problems/isomorphic-strings/
"""


class Solution:
    @staticmethod
    def isIsomorphic(s: str, t: str) -> bool:
        s_t_mapping = {}
        t_s_mapping = {}
        s_length = len(s)
        for i in range(s_length):
            if s[i] not in s_t_mapping:
                s_t_mapping[s[i]] = t[i]
            if s_t_mapping[s[i]] != t[i]:
                return False
        for i in range(s_length):
            if t[i] not in t_s_mapping:
                t_s_mapping[t[i]] = s[i]
            if t_s_mapping[t[i]] != s[i]:
                return False
        return True


assert Solution.isIsomorphic(s="egg", t="add") is True
assert Solution.isIsomorphic(s="foo", t="bar") is False
assert Solution.isIsomorphic(s="paper", t="title") is True
assert Solution.isIsomorphic(s="badr", t="biby") is False
