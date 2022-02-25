"""
https://leetcode.com/problems/compare-version-numbers/
"""


class Solution:
    @staticmethod
    def compare_version(version1: str, version2: str) -> int:
        v1, v2 = version1.split('.'), version2.split('.')
        v1_l, v2_l = len(v1), len(v2)
        for i in range(max(v1_l, v2_l)):
            v1i = v2i = 0
            if i < v1_l:
                v1i = int(v1[i])
            if i < v2_l:
                v2i = int(v2[i])
            if v1i > v2i:
                return 1
            elif v1i < v2i:
                return -1
        return 0


assert Solution.compare_version(version1="1.01", version2="1.001") == 0
assert Solution.compare_version(version1="1.0", version2="1.0.0") == 0
assert Solution.compare_version(version1="0.1", version2="1.1") == -1

"""
"1.01"
"1.001"
"1.0"
"1.0.0"
"0.1"
"1.1"
"1.1"
"0.1"
"0.1"
"1"
"""
