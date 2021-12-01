"""
https://leetcode.com/problems/longest-palindrome/
"""

from collections import Counter


class Solution:
    @staticmethod
    def longestPalindrome(s: str) -> int:
        characters = Counter(s)
        even = odd = 0
        for c in characters:
            if characters[c] % 2 == 0:
                even += characters[c]
            else:
                even += characters[c] - 1
                odd = 1
        return even + odd


assert Solution.longestPalindrome("abccccdd") == 7
"""
Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""
assert Solution.longestPalindrome("a") == 1
assert Solution.longestPalindrome("bb") == 2
assert Solution.longestPalindrome("ccc") == 3
assert Solution.longestPalindrome("ccCCCc") == 5
assert Solution.longestPalindrome("vvvabccccddvv") == 11
