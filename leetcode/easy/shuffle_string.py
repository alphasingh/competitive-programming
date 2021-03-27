"""
https://leetcode.com/problems/shuffle-string/
"""


class Solution:
    @staticmethod
    def restoreString(s: str, indices: [int]) -> str:
        restored = list(s)
        for enumerator, index in enumerate(indices):
            restored[index] = s[enumerator]
        return "".join(restored)


assert Solution.restoreString(s="codeleet", indices=[4, 5, 6, 7, 0, 2, 1, 3]) == "leetcode"
assert Solution.restoreString(s="abc", indices=[0, 1, 2]) == "abc"
assert Solution.restoreString(s="aiohn", indices=[3, 1, 4, 2, 0]) == "nihao"
assert Solution.restoreString(s="aaiougrt", indices=[4, 0, 2, 6, 7, 3, 1, 5]) == "arigatou"
assert Solution.restoreString(s="art", indices=[1, 0, 2]) == "rat"
