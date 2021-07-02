"""
https://leetcode.com/problems/k-th-symbol-in-grammar/
"""


class Solution:
    @staticmethod
    def kthGrammar(n: int, k: int) -> int:
        return bin(k - 1).count('1') & 1


sol = Solution()
"""
Explanation: row 1: 0
"""
assert sol.kthGrammar(n=2, k=1) == 0
"""
Explanation:
row 1: 0
row 2: 01
"""
assert sol.kthGrammar(n=2, k=2) == 1
"""
Explanation:
row 1: 0
row 2: 01
"""
assert sol.kthGrammar(n=3, k=1) == 0
"""
Explanation:
row 1: 0
row 2: 01
row 3: 0110
"""
