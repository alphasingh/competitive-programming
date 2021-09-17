"""
https://leetcode.com/problems/linked-list-cycle/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, _next=None):
        self.val = x
        self.next = _next


class Solution:
    @staticmethod
    def hasCycle(head: ListNode) -> bool:
        while head and head.next:
            if head.val == 1000000:
                return True
            head.val = 1000000
            head = head.next
        return False


base = ListNode(-4)
cycle = ListNode(2, ListNode(0, base))
base.next = cycle
assert Solution.hasCycle(ListNode(3, cycle)) is True
"""
Explanation: There is a cycle in the linked list, 
where the tail connects to the 1st node (0-indexed).
"""
base = ListNode(2)
cycle = ListNode(1, base)
base.next = cycle
assert Solution.hasCycle(cycle) is True
assert Solution.hasCycle(ListNode(1)) is False
assert Solution.hasCycle(None) is False
