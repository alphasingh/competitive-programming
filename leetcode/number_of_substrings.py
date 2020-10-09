"""
1513. Number of Substrings With Only 1s
https://leetcode.com/problems/number-of-substrings-with-only-1s/
"""


class Solution:
    @staticmethod
    def numSub(s: str) -> int:
        sub = 0
        ones = s.split('0')
        for one in ones:
            n = len(one)
            sub += (n * (n + 1)) // 2
        return int(sub % (1e9 + 7))


assert Solution.numSub(s="0110111") == 9
assert Solution.numSub(s="101") == 2
assert Solution.numSub(s="111111") == 21
assert Solution.numSub(s="000") == 0

"""
Examples:

Input: s = "0110111"
Output: 9
Explanation: There are 9 substring in total with only 1's characters.
"1" -> 5 times.
"11" -> 3 times.
"111" -> 1 time.

Input: s = "101"
Output: 2
Explanation: Substring "1" is shown 2 times in s.

Input: s = "111111"
Output: 21
Explanation: Each substring contains only 1's characters.

Input: s = "000"
Output: 0

Hint:
Count number of 1s in each consecutive-1 group. 
For a group with n consecutive 1s, the total contribution of it to the final answer is (n + 1) * n // 2.
"""
