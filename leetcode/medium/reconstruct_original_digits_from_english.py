"""
https://leetcode.com/problems/reconstruct-original-digits-from-english/
"""

from collections import Counter


class Solution:
    DIGITS = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
    ALPHABETS = 'abcdefghijklmnopqrstuvwxyz'

    @staticmethod
    def originalDigits(s: str) -> str:
        c = [1] * 10  # count for 0-9 digits
        output = ''  # final output
        s_alphabets = {alphabet: 0 for alphabet in Solution.ALPHABETS}
        print(s_alphabets)
        digit_dictionary = {digit: Counter(digit) for digit in Solution.DIGITS}
        print(digit_dictionary)
        for digit in range(10):
            output += str(digit) * c[digit]
        print(output)
        return output


# '0'*c[0] + '1'*c[1] + '2'*c[2] + '3'*c[3] + '4'*c[4] + '5'*c[5] + '6'*c[6] + '7'*c[7] + '8'*c[8] + '9'*c[9]


assert Solution.originalDigits("owoztneoer") is "012"
assert Solution.originalDigits("fviefuro") is "45"
