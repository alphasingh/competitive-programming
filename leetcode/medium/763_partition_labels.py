"""
https://leetcode.com/problems/partition-labels/
"""


class Solution:

    @staticmethod
    def partitionLabels(S: str) -> [int]:
        partitions = [-1]
        indexes = {alphabet: list() for alphabet in set(S)}
        for index, alphabet in enumerate(S):
            indexes[alphabet].append(index)
        # print(indexes)
        start = end = 0
        # print(len(S), S)
        while start <= end < len(S):
            # print('start', start, 'end', end, 'current', S[start], indexes[S[start]][-1])
            end = max(end, indexes[S[start]][-1])
            if start == end:  # partition complete
                partitions.append(end)
                # print(partitions)
                start = end + 1
                end = start
            else:
                start += 1
        # print(partition_lengths)
        return [partitions[i + 1] - partitions[i] for i in range(len(partitions) - 1)]


assert Solution.partitionLabels(S="ababcbacadefegdehijhklij") == [9, 7, 8]
"""
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
"""
assert Solution.partitionLabels(S="abcd") == [1, 1, 1, 1]
