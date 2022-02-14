"""
https://codeforces.com/contest/1634/problem/A
"""


class Solution:
    @staticmethod
    def revConcat(n: int, k: int, s: str) -> int:
        p = set()
        k = min(k, 5)

        def dfs(c, d):
            if d == k:
                p.add(c)
                return c
            dfs(c + c[::-1], d + 1)
            dfs(c[::-1] + c, d + 1)

        dfs(s, 0)
        # print(p)
        return len(p)


assert Solution.revConcat(3, 2, "aab") == 2
assert Solution.revConcat(3, 3, "aab") == 2
assert Solution.revConcat(3, 5, "aab") == 2
assert Solution.revConcat(7, 1, "abacaba") == 1
assert Solution.revConcat(2, 0, "ab") == 1

for TC in range(int(input())):
    N, K = map(int, input().split())
    S = input()
    print(Solution.revConcat(N, K, S))

"""
4
3 2
aab
3 3
aab
7 1
abacaba
2 0
ab
-----------------------------------
2
2
1
1
"""
