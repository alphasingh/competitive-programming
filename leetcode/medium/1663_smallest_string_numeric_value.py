"""
https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/
"""


class Solution:
    @staticmethod
    def getSmallestString(n: int, k: int) -> str:
        string = [1] * n
        remainder = k - n
        # improve from O(n)
        for i in range(n - 1, -1, -1):
            if remainder > 25:
                remainder -= 25
                string[i] = 26
            else:
                string[i] += remainder
                remainder = 0
            if remainder == 0:
                break
        return ''.join(chr(ord('a') + string[i] - 1) for i in range(n))


assert Solution.getSmallestString(n=3, k=27) == "aay"
"""
Explanation: The numeric value of the string is 1 + 1 + 25 = 27, 
and it is the smallest string with such a value and length equal to 3.
"""
assert Solution.getSmallestString(n=5, k=73) == "aaszz"
