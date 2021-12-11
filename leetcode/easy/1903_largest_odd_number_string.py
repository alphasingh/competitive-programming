"""
https://leetcode.com/problems/largest-odd-number-in-string/
"""


class Solution:
    @staticmethod
    def largestOddNumber(num: str) -> str:
        last_odd_index = -1
        length_of_num = len(num)
        for i in range(length_of_num - 1, -1, -1):
            if num[i] in '13579':
                last_odd_index = i
                break
        return num[:last_odd_index + 1]


assert Solution.largestOddNumber("52") == "5"
"""
Explanation: The only non-empty substrings are "5", "2", and "52". "5" is the only odd number.
"""
assert Solution.largestOddNumber("4206") == ""
"""
Explanation: There are no odd numbers in "4206".
"""
assert Solution.largestOddNumber("35427") == "35427"
"""
Explanation: "35427" is already an odd number.
"""
