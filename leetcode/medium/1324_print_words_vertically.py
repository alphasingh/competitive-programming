"""
https://leetcode.com/problems/print-words-vertically/
"""


class Solution:
    @staticmethod
    def printVertically(s: str) -> [str]:
        words = s.split()
        width = len(words)
        length = 0
        for word in words:
            length = max(len(word), length)
        # print(length, width)
        final = [[" "] * width for i in range(length)]
        # print(final)
        i = j = 0
        for ch in s:
            if ch == " ":
                i = 0
                j += 1
            else:
                final[i][j] = ch
                i += 1
        # print(final)
        for index, word in enumerate(final):
            final[index] = "".join(word).rstrip()
        return final


assert Solution.printVertically("HOW ARE YOU") == ["HAY", "ORO", "WEU"]
assert Solution.printVertically("TO BE OR NOT TO BE") == ["TBONTB", "OEROOE", "   T"]
assert Solution.printVertically("CONTEST IS COMING") == ["CIC", "OSO", "N M", "T I", "E N", "S G", "T"]
