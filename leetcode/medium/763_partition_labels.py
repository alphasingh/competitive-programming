"""
https://leetcode.com/problems/partition-labels/
"""


class Solution:

    @staticmethod
    def partitionLabels(S: str) -> [int]:
        partitions = [-1]
        return partitions[1:]  # exclude -1


assert Solution.partitionLabels(S="ababcbacadefegdehijhklij") == [9, 7, 8]
"""
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
"""
assert Solution.partitionLabels(S="abcd") == [1, 1, 1, 1]
