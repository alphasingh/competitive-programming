"""
https://leetcode.com/problems/delete-characters-to-make-fancy-string/
"""


class Solution:
    @staticmethod
    def makeFancyString(s: str) -> str:
        stack = ['']
        count = 0
        for ch in s:
            if ch != stack[-1]:
                count = 1
            elif count < 2:
                count += 1
            else:
                continue
            stack.append(ch)
        return ''.join(stack)


assert Solution.makeFancyString('leeetcode') == 'leetcode'
"""
Explanation:
Remove an 'e' from the first group of 'e's to create "leetcode".
No three consecutive characters are equal, so return "leetcode"
"""
assert Solution.makeFancyString("aaabaaaa") == "aabaa"
"""
Explanation:
Remove an 'a' from the first group of 'a's to create "aabaaaa".
Remove two 'a's from the second group of 'a's to create "aabaa".
No three consecutive characters are equal, so return "aabaa".
"""
assert Solution.makeFancyString("aab") == "aab"
"""
Explanation: No three consecutive characters are equal, so return "aab".
"""
