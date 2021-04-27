"""
https://leetcode.com/problems/partition-labels/
"""


class Solution:

    @staticmethod
    def partitionLabels(S: str) -> [int]:
        partitions = [-1]
        indexes = {alphabet: list() for alphabet in set(S)}
        [indexes[alphabet].append(index) for index, alphabet in enumerate(S)]
        start = end = 0
        while start <= end < len(S):
            end = max(end, indexes[S[start]][-1])
            if start == end:  # partition complete
                partitions.append(end)
                start = end + 1
                end = start
            else:
                start += 1
        return [y - x for y, x in zip(partitions[1:], partitions)]


assert Solution.partitionLabels(S="ababcbacadefegdehijhklij") == [9, 7, 8]
"""
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
"""
assert Solution.partitionLabels(S="abcd") == [1, 1, 1, 1]
assert Solution.partitionLabels(S="a") == [1]
assert Solution.partitionLabels(S="aaaaaaaazzzzaaaaaaaaaaa") == [23]
assert Solution.partitionLabels(S="aaaaaaaazzzzaaaaaaaaaaaf") == [23, 1]
