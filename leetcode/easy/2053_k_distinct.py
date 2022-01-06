"""
https://leetcode.com/problems/kth-distinct-string-in-an-array/
"""

from collections import Counter


class Solution:
    @staticmethod
    def kthDistinct(arr: [str], k: int) -> str:
        c = Counter(arr)
        d = []
        for s in arr:
            if c[s] == 1:
                d.append(s)
        return d[k - 1] if len(d) >= k else ""


assert Solution.kthDistinct(arr=["d", "b", "c", "b", "c", "a"], k=2) == "a"
"""
Explanation:
The only distinct strings in arr are "d" and "a".
"d" appears 1st, so it is the 1st distinct string.
"a" appears 2nd, so it is the 2nd distinct string.
Since k == 2, "a" is returned. 
"""
assert Solution.kthDistinct(arr=["aaa", "aa", "a"], k=1) == "aaa"
"""
Explanation:
All strings in arr are distinct, so the 1st string "aaa" is returned.
"""
assert Solution.kthDistinct(arr=["a", "b", "a"], k=3) == ""
"""
Explanation:
The only distinct string is "b". 
Since there are fewer than 3 distinct strings, we return an empty string "".
"""
