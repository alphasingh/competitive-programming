"""
https://leetcode.com/problems/sort-list/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    @staticmethod
    def convert_to_linked_list(array: [int]) -> ListNode:
        return

    @staticmethod
    def sortList(head: ListNode = None) -> ListNode:
        if not head:
            return head
        current = head
        array = []
        while current:
            array.append(current.val)
            current = current.next
        print(array, 'sorted', sorted(array))
        return head


assert Solution.sortList(ListNode(4, ListNode(2, ListNode(1, ListNode(3)))))
assert Solution.sortList(ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0))))))
assert Solution.sortList(None) is None
