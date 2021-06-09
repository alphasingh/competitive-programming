"""
https://leetcode.com/problems/merge-two-sorted-lists/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, _next=None):
        self.val = val
        self.next = _next


class Solution:
    @staticmethod
    def mergeTwoLists(l1, l2):
        if not l1 and not l2:
            return None
        return ListNode()


assert Solution.mergeTwoLists(None, None) is None
