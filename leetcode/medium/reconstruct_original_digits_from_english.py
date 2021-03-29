"""
https://leetcode.com/problems/reconstruct-original-digits-from-english/
"""

from collections import Counter


class Solution:
    DIGITS_OUTPUT = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
                     'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    #           g       x       w       z       t       u       f       s       i       o
    DIGITS = ('eight', 'six', 'two', 'zero', 'three', 'four', 'five', 'seven', 'nine', 'one')
    SORTED_DIGITS = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
    ALPHABETS = 'abcdefghijklmnopqrstuvwxyz'

    @staticmethod
    def originalDigits(jumbled_word: str) -> str:
        digit_count = {digit: 0 for digit in Solution.DIGITS}  # count for 0-9 digits
        output = ''  # final output
        jumbled_word_dictionary = {alphabet: 0 for alphabet in Solution.ALPHABETS}
        for char in jumbled_word:
            jumbled_word_dictionary[char] += 1
        # print(jumbled_word_dictionary)
        digit_dictionary = {digit: Counter(digit) for digit in Solution.DIGITS}
        # print(digit_dictionary)
        for digit in Solution.DIGITS:
            current_dictionary = digit_dictionary[digit]
            digit_minimum_count = 50000
            for alphabet in current_dictionary:
                alphabet_count = jumbled_word_dictionary[alphabet] // current_dictionary[alphabet]
                digit_minimum_count = min(digit_minimum_count, alphabet_count)
            if digit_minimum_count > 0:
                for alphabet in current_dictionary:
                    jumbled_word_dictionary[alphabet] -= current_dictionary[alphabet] * digit_minimum_count
            digit_count[digit] = digit_minimum_count
        for sorted_digit in Solution.SORTED_DIGITS:
            output += Solution.DIGITS_OUTPUT[sorted_digit] * digit_count[sorted_digit]
        # print(output)
        return output


# '0'*c[0] + '1'*c[1] + '2'*c[2] + '3'*c[3] + '4'*c[4] + '5'*c[5] + '6'*c[6] + '7'*c[7] + '8'*c[8] + '9'*c[9]


assert Solution.originalDigits("eezertwooononnine") == "01129"
assert Solution.originalDigits("owoztneoer") == "012"
assert Solution.originalDigits("fviefuro") == "45"
assert Solution.originalDigits("zeroonetwothreefourfivesixseveneightnine") == "0123456789"
assert Solution.originalDigits("toontohenfeverwisezensixervine") == "0235679"
