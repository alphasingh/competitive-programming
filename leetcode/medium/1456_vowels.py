"""
https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
"""


class Solution:
    @staticmethod
    def maxVowels(s: str, k: int) -> int:
        v = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
        n = len(s)
        w = s[:k]
        # print(w)
        r = 0
        for c in w:
            if c in v:
                r += 1
        # print(w)
        m = r
        for i in range(1, n - k + 1):
            # print('-', s[i-1], '+', s[i-1+k])
            if s[i - 1] in v:
                r -= 1
            if s[i - 1 + k] in v:
                r += 1
            m = max(m, r)
        return m


assert Solution.maxVowels(s="abciiidef", k=3) == 3
# Explanation: The substring "iii" contains 3 vowel letters.
assert Solution.maxVowels(s="aeiou", k=2) == 2
# Explanation: Any substring of length 2 contains 2 vowels.
assert Solution.maxVowels(s="leetcode", k=3) == 2
# Explanation: "lee", "eet" and "ode" contain 2 vowels.
