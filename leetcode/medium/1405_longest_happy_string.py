"""
https://leetcode.com/problems/longest-happy-string/
"""


class Solution:
    @staticmethod
    def longestDiverseString(a: int, b: int, c: int) -> str:
        abc = [[a, 'a'], [b, 'b'], [c, 'c']]
        stack = ['']
        cont = 1
        while True:
            abc.sort()  # on basis of count
            # print(abc)
            last = abc[-1]
            if last[0] == 0:
                break
            if stack[-1] == last[1]:
                cont += 1
            if cont == 3 and abc[1][0] == 0 and abc[0][0] == 0:
                break
            if cont == 3:
                second = abc[1]
                stack.append(second[1])
                abc[1][0] -= 1
                cont = 1
            else:
                abc[2][0] -= 1
                stack.append(last[1])
            # print(stack)
        return ''.join(stack)


assert Solution.longestDiverseString(a=1, b=1, c=7) == "ccbccacc"
assert Solution.longestDiverseString(a=7, b=1, c=0) == "aabaa"
assert Solution.longestDiverseString(a=100, b=0, c=0) == "aa"
