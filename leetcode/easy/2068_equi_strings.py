"""
https://leetcode.com/problems/check-whether-two-strings-are-almost-equivalent/
"""

from collections import Counter


class Solution:
    @staticmethod
    def checkAlmostEquivalent(word1: str, word2: str) -> bool:
        w1c, w2c = Counter(word1), Counter(word2)
        for char in 'abcdefghijklmnopqrstuvwxyz':
            v1 = v2 = 0
            if char in w2c:
                v2 = w2c[char]
            if char in w1c:
                v1 = w1c[char]
            if abs(v1 - v2) > 3:
                return False
        return True


assert Solution.checkAlmostEquivalent(word1="aaaa", word2="bccb") is False
"""
Explanation: There are 4 'a's in "aaaa" but 0 'a's in "bccb".
The difference is 4, which is more than the allowed 3.
"""
assert Solution.checkAlmostEquivalent(word1="abcdeef", word2="abaaacc") is True
"""
Explanation: The differences between the frequencies of each letter in word1 and word2 are at most 3:
- 'a' appears 1 time in word1 and 4 times in word2. The difference is 3.
- 'b' appears 1 time in word1 and 1 time in word2. The difference is 0.
- 'c' appears 1 time in word1 and 2 times in word2. The difference is 1.
- 'd' appears 1 time in word1 and 0 times in word2. The difference is 1.
- 'e' appears 2 times in word1 and 0 times in word2. The difference is 2.
- 'f' appears 1 time in word1 and 0 times in word2. The difference is 1.
"""
assert Solution.checkAlmostEquivalent(word1="cccddabba", word2="babababab") is True
"""
Explanation: The differences between the frequencies of each letter in word1 and word2 are at most 3:
- 'a' appears 2 times in word1 and 4 times in word2. The difference is 2.
- 'b' appears 2 times in word1 and 5 times in word2. The difference is 3.
- 'c' appears 3 times in word1 and 0 times in word2. The difference is 3.
- 'd' appears 2 times in word1 and 0 times in word2. The difference is 2.
"""
