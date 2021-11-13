"""
https://leetcode.com/problems/long-pressed-name/
"""


class Solution:
    @staticmethod
    def isLongPressedName(name: str, typed: str) -> bool:
        name += '#'
        typed += '#'
        name_sequence = []
        typed_sequence = []
        current_char = 'A'
        current_count = 0
        for char in name:
            if char != current_char:
                name_sequence.append([current_char, current_count])
                current_char = char
                current_count = 1
            else:
                current_count += 1
        current_char = 'A'
        current_count = 0
        for char in typed:
            if char != current_char:
                typed_sequence.append([current_char, current_count])
                current_char = char
                current_count = 1
            else:
                current_count += 1
        # print(name_sequence)
        # print(typed_sequence)
        sequence_size = len(typed_sequence)
        if sequence_size != len(name_sequence):
            return False
        for i in range(sequence_size):
            if name_sequence[i][0] != typed_sequence[i][0]:
                return False
            if name_sequence[i][1] > typed_sequence[i][1]:
                return False
        return True


assert Solution.isLongPressedName(name="alex", typed="aaleex") is True
# Explanation: 'a' and 'e' in 'alex' were long pressed.
assert Solution.isLongPressedName(name="leelee", typed="lleeelee") is True
assert Solution.isLongPressedName(name="saeed", typed="ssaaedd") is False
# Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.
assert Solution.isLongPressedName(name="laiden", typed="laiden") is True
# Explanation: It's not necessary to long press any character.
