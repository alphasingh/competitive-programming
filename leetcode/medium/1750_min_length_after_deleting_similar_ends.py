"""
https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/
"""


class Solution:
    @staticmethod
    def minimumLength(s: str) -> int:
        length = len(s)
        deletions = 0
        f = [['z', 0]]
        for char in s:
            if f[-1][0] != char:
                f.append([char, 0])
            f[-1][1] += 1
        f = f[1:]  # remove z from the start
        # print(f)
        frequencies = len(f)
        left = 0
        right = frequencies - 1
        while left <= right:
            if f[left][0] == f[right][0]:
                deletions += f[left][1] + f[right][1]
                left += 1
                right -= 1
            else:
                break
        remaining = length - deletions
        if remaining < 0:  # palindrome and intersection
            return 0 if f[frequencies // 2][1] > 1 else 1
        return remaining


assert Solution.minimumLength("ca") == 2
"""
Explanation: You can't remove any characters, so the string stays as is.
"""
assert Solution.minimumLength("cabaabac") == 0
"""
Explanation: An optimal sequence of operations is:
- Take prefix = "c" and suffix = "c" and remove them, s = "abaaba".
- Take prefix = "a" and suffix = "a" and remove them, s = "baab".
- Take prefix = "b" and suffix = "b" and remove them, s = "aa".
- Take prefix = "a" and suffix = "a" and remove them, s = "".
"""
assert Solution.minimumLength("aabccabba") == 3
"""
Explanation: An optimal sequence of operations is:
- Take prefix = "aa" and suffix = "a" and remove them, s = "bccabb".
- Take prefix = "b" and suffix = "bb" and remove them, s = "cca".
"""
assert Solution.minimumLength("a") == 1
assert Solution.minimumLength("bbb") == 0
"""
"ca"
"cabaabac"
"cababac"
"aabccabba"
"a"
"bbb"
"""
