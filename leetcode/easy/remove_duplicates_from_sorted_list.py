"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list/
"""


class Solution:
    @staticmethod
    def deleteDuplicates(head: [int]) -> [int]:
        return head


assert Solution.deleteDuplicates(head=[1, 1, 2]) == [1, 2]
assert Solution.deleteDuplicates(head=[1, 1, 2, 3, 3]) == [1, 2, 3]
