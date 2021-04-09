"""
https://leetcode.com/problems/verifying-an-alien-dictionary/
"""


class Solution:

    @staticmethod
    def isAlienSorted(words: [str], order: str) -> bool:
        value = {alphabet: position for position, alphabet in enumerate(order)}
        value_of_words = [[value[alphabet] for alphabet in word] for word in words]
        return sorted(value_of_words) == value_of_words


assert Solution.isAlienSorted(words=["hello", "leetcode"], order="hlabcdefgijkmnopqrstuvwxyz") is True
# Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
assert Solution.isAlienSorted(words=["word", "world", "row"], order="worldabcefghijkmnpqstuvxyz") is False
# Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
assert Solution.isAlienSorted(words=["apple", "app"], order="abcdefghijklmnopqrstuvwxyz") is False
"""
Explanation: The first three characters "app" match, and the second string is shorter (in size.) 
According to lexicographical rules "apple" > "app", because 'l' > '∅', 
where '∅' is defined as the blank character which is less than any other character (More info).
"""
