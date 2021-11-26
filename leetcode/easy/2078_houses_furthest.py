"""
https://leetcode.com/problems/two-furthest-houses-with-different-colors/
"""


class Solution:
    @staticmethod
    def maxDistance(colors: [int]) -> int:
        m = 0
        n = len(colors)
        for i in range(n):
            for j in range(i + 1, n):
                if colors[i] != colors[j]:
                    m = max(m, abs(i - j))
        return m


assert Solution.maxDistance([1, 1, 1, 6, 1, 1, 1]) == 3
"""
Explanation: In the above image, color 1 is blue, and color 6 is red.
The furthest two houses with different colors are house 0 and house 3.
House 0 has color 1, and house 3 has color 6. The distance between them is abs(0 - 3) = 3.
Note that houses 3 and 6 can also produce the optimal answer.
"""
assert Solution.maxDistance([1, 8, 3, 8, 3]) == 4
"""
Explanation: In the above image, color 1 is blue, color 8 is yellow, and color 3 is green.
The furthest two houses with different colors are house 0 and house 4.
House 0 has color 1, and house 4 has color 3. The distance between them is abs(0 - 4) = 4.
"""
assert Solution.maxDistance([0, 1]) == 1
"""
Explanation: The furthest two houses with different colors are house 0 and house 1.
House 0 has color 0, and house 1 has color 1. The distance between them is abs(0 - 1) = 1.
"""
