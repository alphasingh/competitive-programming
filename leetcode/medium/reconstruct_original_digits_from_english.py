"""
https://leetcode.com/problems/reconstruct-original-digits-from-english/
"""

from collections import Counter


class Solution:
    DIGITS = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
    ALPHABETS = 'abcdefghijklmnopqrstuvwxyz'

    @staticmethod
    def originalDigits(jumbled_word: str) -> str:
        digit_count = {digit: 0 for digit in Solution.DIGITS}  # count for 0-9 digits
        output = ''  # final output
        jumbled_word_dictionary = {alphabet: 0 for alphabet in Solution.ALPHABETS}
        for char in jumbled_word:
            jumbled_word_dictionary[char] += 1
        print(jumbled_word_dictionary)
        digit_dictionary = {digit: Counter(digit) for digit in Solution.DIGITS}
        print(digit_dictionary)
        for digit in digit_dictionary:
            current_dictionary = digit_dictionary[digit]
            digit_minimum_count = 50000
            for alphabet in current_dictionary:
                alphabet_count = jumbled_word_dictionary[alphabet] // current_dictionary[alphabet]
                digit_minimum_count = min(digit_minimum_count, alphabet_count)
            digit_count[digit] = digit_minimum_count
        for i, digit in enumerate(Solution.DIGITS):
            output += str(i) * digit_count[digit]
        print(output)
        return output


# '0'*c[0] + '1'*c[1] + '2'*c[2] + '3'*c[3] + '4'*c[4] + '5'*c[5] + '6'*c[6] + '7'*c[7] + '8'*c[8] + '9'*c[9]


assert Solution.originalDigits("owoztneoer") == "012"
assert Solution.originalDigits("fviefuro") == "45"
