"""
https://leetcode.com/problems/count-vowels-permutation/
"""


class Solution:
    @staticmethod
    def countVowelPermutation(n: int) -> int:
        a = e = i = o = u = 1
        mod = 1000000007
        for _ in range(n - 1):
            a, e, i, o, u = (e + i + u) % mod, (a + i) % mod, (e + o) % mod, i % mod, (i + o) % mod
        return (a + e + i + o + u) % mod


assert Solution.countVowelPermutation(1) == 5
"""
Explanation: All possible strings are: "a", "e", "i" , "o" and "u".
"""
assert Solution.countVowelPermutation(2) == 10
"""
Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".
"""
assert Solution.countVowelPermutation(5) == 68
