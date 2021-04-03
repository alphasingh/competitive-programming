"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
"""

from collections import Counter


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val) + "->" + str(self.next)


class Solution:
    @staticmethod
    def deleteDuplicates(head: ListNode) -> ListNode:
        return head

    @staticmethod
    def deleteDuplicates_list(head: [int]) -> [int]:
        counter = Counter(head)
        one_timers = []
        for key in counter:
            if counter[key] == 1:  # only one occurrence, i.e. no duplicate
                one_timers.append(key)
        return one_timers


assert Solution.deleteDuplicates_list(head=[1, 2, 3, 3, 4, 4, 5]) == [1, 2, 5]
assert Solution.deleteDuplicates_list(head=[1, 1, 1, 2, 3]) == [2, 3]
