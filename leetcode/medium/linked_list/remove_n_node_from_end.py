"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val) + "->" + str(self.next)


class Solution:

    @staticmethod
    def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
        print(n)
        print(head)
        return head


linked_list = ListNode(1, next=ListNode(2, next=ListNode(3, next=ListNode(4, next=ListNode(5)))))
assert Solution.removeNthFromEnd(head=linked_list, n=2)

assert Solution.removeNthFromEnd(head=ListNode(1), n=1)

assert Solution.removeNthFromEnd(head=ListNode(1, next=ListNode(2)), n=1)
