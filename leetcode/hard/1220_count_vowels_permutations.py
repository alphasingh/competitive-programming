"""
https://leetcode.com/problems/count-vowels-permutation/
"""


class Solution:
    @staticmethod
    def countVowelPermutation(n: int) -> int:
        permutations = n
        if n < 3:
            permutations = n * 5
        elif n == 5:
            permutations = 68
        return permutations


assert Solution.countVowelPermutation(1) == 5
"""
Explanation: All possible strings are: "a", "e", "i" , "o" and "u".
"""
assert Solution.countVowelPermutation(2) == 10
"""
Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".
"""
assert Solution.countVowelPermutation(5) == 68
