"""
https://leetcode.com/problems/find-all-anagrams-in-a-string/
"""


class Solution:
    ALPHABETS = 'abcdefghijklmnopqrstuvwxyz'

    def findAnagrams(self, s: str, p: str) -> [int]:
        string_length = len(s)
        anagram_length = len(p)
        current_string = s[:anagram_length]
        current_counter = {alphabet: 0 for alphabet in self.ALPHABETS}
        anagram_counter = {alphabet: 0 for alphabet in self.ALPHABETS}
        for char in current_string:
            current_counter[char] += 1
        for char in p:
            anagram_counter[char] += 1
        anagrams = [0] if anagram_counter == current_counter else []
        for i in range(1, string_length - anagram_length + 1):
            # print(i, current_counter, s[i-1])
            current_counter[s[i - 1]] -= 1
            new_char = s[i + anagram_length - 1]
            # print(s[i-1], new_char)
            current_counter[new_char] += 1
            # print(i, current_counter)
            if current_counter == anagram_counter:
                anagrams.append(i)
        return anagrams


sol = Solution()
assert sol.findAnagrams("cbaebabacd", "abc") == [0, 6]
"""
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
"""
assert sol.findAnagrams("abab", "ab") == [0, 1, 2]
"""
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""
