"""
https://leetcode.com/problems/hamming-distance/
"""


class Solution:
    @staticmethod
    def hammingDistance(x: int, y: int) -> int:
        x, y = bin(x), bin(y)
        # print(x, y)
        x, y = x[2:], y[2:]
        # print(x, y)
        l_x, l_y = len(x), len(y)
        # print(l_x, l_y)
        m_l = max(l_x, l_y)
        x = x.zfill(m_l)
        y = y.zfill(m_l)
        # print(x, y)
        d = 0
        for i in range(m_l):
            if x[i] != y[i]:
                d += 1
        return d


assert Solution.hammingDistance(x=1, y=4) == 2
"""
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.
"""
assert Solution.hammingDistance(x=3, y=1) == 1
