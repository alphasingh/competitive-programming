"""
https://leetcode.com/problems/count-sorted-vowel-strings/
"""

from itertools import combinations_with_replacement


class Solution:
    @staticmethod
    def countVowelStrings(n: int) -> int:  # brute force needs to be improved
        count = 0
        vowels = 'aeiou'
        combinations_with_replacement_of_size_n = list(combinations_with_replacement(vowels, n))
        print(combinations_with_replacement_of_size_n)
        for combination in combinations_with_replacement_of_size_n:
            print(sorted(combination), combination)
            if sorted(combination) == list(combination):
                count += 1
        return count


assert Solution.countVowelStrings(1) == 5
"""
Explanation: The 5 sorted strings that consist of vowels only are ["a","e","i","o","u"].
"""
assert Solution.countVowelStrings(2) == 15
"""
Explanation: The 15 sorted strings that consist of vowels only are
["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.
"""
assert Solution.countVowelStrings(33) == 66045
