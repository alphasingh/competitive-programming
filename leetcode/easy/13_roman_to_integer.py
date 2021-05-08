"""
https://leetcode.com/problems/roman-to-integer/
"""


class Solution:
    value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def romanToInt(self, s: str) -> int:
        output = 0
        for i in range(len(s) - 2, -1, -1):
            if self.value[s[i]] < self.value[s[i + 1]]:
                output -= self.value[s[i]]
            else:
                output += self.value[s[i]]
        output += self.value[s[-1]]
        return output


solution = Solution()
assert solution.romanToInt("III") == 3
assert solution.romanToInt("IV") == 4
assert solution.romanToInt("IX") == 9
assert solution.romanToInt("LVIII") == 58
# Explanation: L = 50, V= 5, III = 3.
assert solution.romanToInt("MCMXCIV") == 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
