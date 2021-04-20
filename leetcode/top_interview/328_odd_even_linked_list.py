"""
https://leetcode.com/problems/odd-even-linked-list/
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
    def oddEvenList(head: ListNode) -> ListNode:
        result = head
        return result


example_in = ListNode(1, next=ListNode(2, next=ListNode(3, next=ListNode(4, next=ListNode(5)))))
example_out = ListNode(1, next=ListNode(2, next=ListNode(3, next=ListNode(4, next=ListNode(5)))))
assert str(Solution.oddEvenList(example_in)) == '1->2->3->4->5->None'
# assert str(Solution.oddEvenList(example_in)) == '1->3->5->2->4->None'
