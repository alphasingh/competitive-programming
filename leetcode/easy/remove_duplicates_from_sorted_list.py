"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list/
"""


class Solution:
    @staticmethod
    def deleteDuplicates(head: [int]) -> [int]:
        uniques = list()
        start = -101
        for element in head:
            if element > start:
                start = element
                uniques.append(element)
        return uniques


assert Solution.deleteDuplicates(head=[1, 1, 2]) == [1, 2]
assert Solution.deleteDuplicates(head=[1, 1, 2, 3, 3]) == [1, 2, 3]
