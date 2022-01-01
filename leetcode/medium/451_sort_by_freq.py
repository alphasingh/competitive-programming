"""
https://leetcode.com/problems/sort-characters-by-frequency/
"""

from collections import Counter
import heapq


class Solution:
    @staticmethod
    def frequencySort(s: str) -> str:
        m = []
        for k, v in Counter(s).items():
            heapq.heappush(m, (-v, k))
        r = ''
        while m:
            v, k = heapq.heappop(m)
            r += k * (-v)
        return r


assert Solution.frequencySort("tree") == "eert"
"""
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
"""
assert Solution.frequencySort("Aabb") == "bbAa"
"""
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
"""
assert Solution.frequencySort("cccaaa") == "aaaccc"
"""
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.
"""
