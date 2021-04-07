"""
https://leetcode.com/problems/determine-if-string-halves-are-alike/
"""


class Solution:
    VOWELS = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

    @staticmethod
    def halvesAreAlike(s: str) -> bool:
        length = len(s)
        first = second = 0
        for i in range(length // 2):
            if s[i] in Solution.VOWELS:
                first += 1
        for i in range(length // 2, length):
            if s[i] in Solution.VOWELS:
                second += 1
        return first == second


assert Solution.halvesAreAlike(s="book") is True
"""
Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.
"""
assert Solution.halvesAreAlike(s="textbook") is False
"""
Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2. Therefore, they are not alike.
Notice that the vowel o is counted twice.
"""
assert Solution.halvesAreAlike(s="MerryChristmas") is False
assert Solution.halvesAreAlike(s="AbCdEfGh") is True
