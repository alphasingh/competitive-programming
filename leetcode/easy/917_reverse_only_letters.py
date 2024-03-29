"""
https://leetcode.com/problems/reverse-only-letters/
"""


class Solution:
    @staticmethod
    def reverseOnlyLetters(s: str) -> str:
        a = list(s)
        start = 0
        end = len(s) - 1
        while start < end:
            start_alpha = s[start].isalpha()
            end_alpha = s[end].isalpha()
            if start_alpha and end_alpha:  # swap for reverse
                a[start], a[end] = a[end], a[start]
            elif start_alpha:
                start -= 1
            elif end_alpha:
                end += 1
            start += 1
            end -= 1
        # print(a)
        return ''.join(map(str, a))


assert Solution.reverseOnlyLetters(s="ab-cd") == "dc-ba"
assert Solution.reverseOnlyLetters(s="a-bC-dEf-ghIj") == "j-Ih-gfE-dCba"
assert Solution.reverseOnlyLetters(s="Test1ng-Leet=code-Q!") == "Qedo1ct-eeLg=ntse-T!"
assert Solution.reverseOnlyLetters(s="7_28]") == "7_28]"
assert Solution.reverseOnlyLetters(s=";2N8op6") == ";2p8oN6"
