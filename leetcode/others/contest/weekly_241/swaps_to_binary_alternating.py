"""
https://leetcode.com/contest/weekly-contest-241/problems/minimum-number-of-swaps-to-make-the-binary-string-alternating/
"""


class Solution:
    @staticmethod
    def minSwaps(s: str) -> int:
        swaps = -1
        zeroes = ones = 0
        size = len(s)
        if size == 1:
            return 0
        # 01 pattern
        pattern = '01' * (size // 2)
        if size % 2 != 0:  # odd
            pattern += '0'
        # print(pattern)
        for i in range(size):
            if s[i] != pattern[i]:
                if s[i] == '0':
                    zeroes += 1
                else:
                    ones += 1
        if zeroes == ones:
            swaps = zeroes
        zeroes = ones = 0
        # 10 pattern
        pattern = '10' * (size // 2)
        if size % 2 != 0:  # odd
            pattern += '1'
        # print(pattern)
        for i in range(size):
            if s[i] != pattern[i]:
                if s[i] == '0':
                    zeroes += 1
                else:
                    ones += 1
        if zeroes == ones:
            if swaps != -1:
                swaps = min(swaps, zeroes)
            else:
                swaps = zeroes
        return swaps


assert Solution.minSwaps("111000") == 1
assert Solution.minSwaps("010") == 0
assert Solution.minSwaps("1110") == -1
assert Solution.minSwaps("1") == 0
assert Solution.minSwaps("10") == 0
assert Solution.minSwaps("01") == 0
assert Solution.minSwaps("11") == -1
assert Solution.minSwaps("0010111") == 1
