"""
https://leetcode.com/problems/replace-the-substring-for-balanced-string/
"""


class Solution:

    @staticmethod
    def balancedString(s: str) -> int:
        length = len(s)
        each_length = length // 4
        substring_length = 1e7
        counter = {'Q': 0, 'W': 0, 'E': 0, 'R': 0}
        left = 0
        right = length - 1
        while left < right:
            left_char = s[left]
            right_char = s[right]
            if counter[left_char] == counter[right_char] == each_length:
                break
            if counter[left_char] < each_length:  # include left
                counter[left_char] += 1
                left += 1
            if counter[left_char] == each_length and counter[right_char] < each_length:  # include right
                counter[right_char] += 1
                right -= 1
        if counter != {'Q': each_length, 'W': each_length, 'E': each_length, 'R': each_length}:
            substring_length = min(substring_length, abs(right - left) + 1)
        else:
            substring_length = 0
        s = s[::-1]
        left = 0
        right = length - 1
        counter = {'Q': 0, 'W': 0, 'E': 0, 'R': 0}
        while left < right:
            left_char = s[left]
            right_char = s[right]
            if counter[left_char] == counter[right_char] == each_length:
                break
            if counter[right_char] < each_length:  # include right
                counter[right_char] += 1
                right -= 1
            if counter[right_char] == each_length and counter[left_char] < each_length:  # include left
                counter[left_char] += 1
                left += 1
        if counter != {'Q': each_length, 'W': each_length, 'E': each_length, 'R': each_length}:
            substring_length = min(substring_length, abs(right - left) + 1)
        else:
            substring_length = 0
        # print(counter)
        left = 0
        right = length - 1
        counter = {'Q': 0, 'W': 0, 'E': 0, 'R': 0}
        while left < right:
            left_char = s[left]
            right_char = s[right]
            if counter[left_char] == counter[right_char] == each_length:
                break
            if counter[right_char] < each_length:  # include right
                counter[right_char] += 1
                right -= 1
            if counter[right_char] == each_length and counter[left_char] < each_length:  # include left
                counter[left_char] += 1
                left += 1
        if counter != {'Q': each_length, 'W': each_length, 'E': each_length, 'R': each_length}:
            substring_length = min(substring_length, abs(right - left) + 1)
        else:
            substring_length = 0
        left = 0
        right = length - 1
        counter = {'Q': 0, 'W': 0, 'E': 0, 'R': 0}
        while left < right:
            left_char = s[left]
            right_char = s[right]
            if counter[left_char] == counter[right_char] == each_length:
                break
            if counter[right_char] < each_length:  # include right
                counter[right_char] += 1
                right -= 1
            if counter[left_char] < each_length:  # include left
                counter[left_char] += 1
                left += 1
        if counter != {'Q': each_length, 'W': each_length, 'E': each_length, 'R': each_length}:
            substring_length = min(substring_length, abs(right - left) + 1)
        else:
            substring_length = 0
        # print(substring_length)
        return substring_length


assert Solution.balancedString(s="QWER") is 0
# Explanation: s is already balanced.
assert Solution.balancedString(s="QQWE") is 1
# Explanation: We need to replace a 'Q' to 'R', so that "RQWE" (or "QRWE") is balanced.
assert Solution.balancedString(s="QQQW") is 2
# Explanation: We can replace the first "QQ" to "ER".
assert Solution.balancedString(s="QQQQ") is 3
# Explanation: We can replace the last 3 'Q' to make s = "QWER".
assert Solution.balancedString(s="WQWRQQQW") is 3
assert Solution.balancedString(s="WWEQERQWQWWRWWERQWEQ") is 4
assert Solution.balancedString(s="RQRERREWEEWWQWRRRWQQEQQQ") is 2

"""
Constraints:
1 <= s.length <= 10^5
s.length is a multiple of 4
s contains only 'Q', 'W', 'E' and 'R'.
"""
