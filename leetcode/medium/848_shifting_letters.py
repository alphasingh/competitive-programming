"""
https://leetcode.com/problems/shifting-letters/
"""


class Solution:
    A = 'abcdefghijklmnopqrstuvwxyz'

    def shiftingLetters(self, s: str, shifts: [int]) -> str:
        length = len(s)
        for i in range(length - 2, -1, -1):
            shifts[i] += shifts[i + 1] % 26
        # print(s)
        # print(shifts)
        for i in range(length - 1, -1, -1):
            shifts[i] = self.A[(ord(s[i]) - ord('a') + shifts[i]) % 26]
        # print(shifts)
        return "".join(shifts)


sol = Solution()
assert sol.shiftingLetters(s="abc", shifts=[3, 5, 9]) == "rpl"
"""
Explanation: We start with "abc".
After shifting the first 1 letters of s by 3, we have "dbc".
After shifting the first 2 letters of s by 5, we have "igc".
After shifting the first 3 letters of s by 9, we have "rpl", the answer.
"""
assert sol.shiftingLetters(s="aaa", shifts=[1, 2, 3]) == "gfd"
