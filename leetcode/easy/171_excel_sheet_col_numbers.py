"""
https://leetcode.com/problems/excel-sheet-column-number/
"""


class Solution:
    @staticmethod
    def titleToNumber(columnTitle: str) -> int:
        length = len(columnTitle)
        number = 0
        for column in range(length):
            value = ord(columnTitle[column]) - 64
            number += value * 26 ** (length - column - 1)
        return number


assert Solution.titleToNumber('A') == 1
assert Solution.titleToNumber('AB') == 28
assert Solution.titleToNumber('ZY') == 701
assert Solution.titleToNumber('FXSHRXW') == 2147483647
