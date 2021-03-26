"""
https://leetcode.com/problems/word-subsets/
"""

from collections import Counter


class Solution:
    @staticmethod
    def wordSubsets(A: [str], B: [str]) -> [str]:
        counter_a = dict()
        counter_b = dict()
        universal_a = list()
        for b in B:
            counter_b[b] = Counter(b)
        for a in A:
            counter_a[a] = Counter(a)
        for a in counter_a:
            is_universal = True
            for b in counter_b:
                for key in b:
                    if (key not in counter_a[a]) or (counter_a[a][key] < counter_b[b][key]):
                        is_universal = False
            if is_universal:
                universal_a.append(a)
        return universal_a


assert Solution.wordSubsets(A=["amazon", "apple", "facebook", "google", "leetcode"],
                            B=["e", "o"]) == ["facebook", "google", "leetcode"]
assert Solution.wordSubsets(A=["amazon", "apple", "facebook", "google", "leetcode"],
                            B=["l", "e"]) == ["apple", "google", "leetcode"]
assert Solution.wordSubsets(A=["amazon", "apple", "facebook", "google", "leetcode"],
                            B=["e", "oo"]) == ["facebook", "google"]
assert Solution.wordSubsets(A=["amazon", "apple", "facebook", "google", "leetcode"],
                            B=["lo", "eo"]) == ["google", "leetcode"]
assert Solution.wordSubsets(A=["amazon", "apple", "facebook", "google", "leetcode"],
                            B=["ec", "oc", "ceo"]) == ["facebook", "leetcode"]
