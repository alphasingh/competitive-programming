"""
https://leetcode.com/problems/k-th-symbol-in-grammar/
"""


class Solution:
    @staticmethod
    def kthGrammar(n: int, k: int) -> int:
        kth_symbol = k + n
        if k % 2 == 0:
            kth_symbol = 1
        elif k % 2 != 0:
            kth_symbol = 0
        return kth_symbol


assert Solution.kthGrammar(n=1, k=1) == 0
"""
Explanation: row 1: 0
"""
assert Solution.kthGrammar(n=2, k=1) == 0
"""
Explanation:
row 1: 0
row 2: 01
"""
assert Solution.kthGrammar(n=2, k=2) == 1
"""
Explanation:
row 1: 0
row 2: 01
"""
assert Solution.kthGrammar(n=3, k=1) == 0
"""
Explanation:
row 1: 0
row 2: 01
row 3: 0110
"""
