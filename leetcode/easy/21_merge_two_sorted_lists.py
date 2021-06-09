"""
https://leetcode.com/problems/merge-two-sorted-lists/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, _next=None):
        self.val = val
        self.next = _next

    def __str__(self):
        return str(self.val) + '>' + str(self.next)


class Solution:
    @staticmethod
    def mergeTwoLists(l1, l2):
        if not l1 and not l2:
            return None
        merged = ListNode()
        merged_pointer = merged
        while l1 or l2:
            if l1 and l2:
                merged_pointer.next = ListNode(l2.val)
                l2 = l2.next
            elif l1:
                merged_pointer.next = ListNode(l1.val)
                l1 = l1.next
            elif l2:
                merged_pointer.next = ListNode(l2.val)
                l2 = l2.next
            merged_pointer = merged_pointer.next
        print(merged)
        print(merged.next)
        return merged.next


assert Solution.mergeTwoLists(None, None) is None
assert str(Solution.mergeTwoLists(None, ListNode(0))) == str(ListNode(0))
