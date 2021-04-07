"""
https://leetcode.com/problems/determine-if-string-halves-are-alike/
"""


class Solution:
    @staticmethod
    def halvesAreAlike(s: str) -> bool:
        return len(s) == 0


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
