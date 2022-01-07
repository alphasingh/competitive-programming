"""
https://naq20.kattis.com/problems/simonsays
"""


class Solution:
    PHRASE_START = 'Simon says '
    PHRASE_LENGTH = 11

    def findCommands(self, s: str):
        if s[:self.PHRASE_LENGTH] == self.PHRASE_START:
            print(s[self.PHRASE_LENGTH:])


solution = Solution()
assert solution.findCommands('Simon says smile.') is None
for T in range(int(input())):
    solution.findCommands(input())
