"""
https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/
"""


class Solution:
    @staticmethod
    def minimumDeletions(s: str) -> int:
        b = s.count('b')
        n = len(s)
        d = b
        for i in range(n - 1, -1, -1):
            if s[i] == 'b':
                b -= 1
                d = min(d, b)
            else:
                b += 1
        return d


assert Solution.minimumDeletions("aababbab") == 2
"""
Explanation: You can either:
Delete the characters at 0-indexed positions 2 and 6 ("aababbab" -> "aaabbb"), or
Delete the characters at 0-indexed positions 3 and 6 ("aababbab" -> "aabbbb").
"""
assert Solution.minimumDeletions("bbaaaaabb") == 2
"""
Explanation: The only solution is to delete the first two characters.
"""
assert Solution.minimumDeletions("a") == 0
assert Solution.minimumDeletions("aaaa") == 0
assert Solution.minimumDeletions("bbba") == 1
assert Solution.minimumDeletions("bbb") == 0
