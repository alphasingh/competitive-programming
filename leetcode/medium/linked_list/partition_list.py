"""
https://leetcode.com/problems/partition-list/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def partition(head: ListNode, x: int) -> ListNode:
        return head


head1 = ListNode(1, next=ListNode(4, next=ListNode(3, next=ListNode(2, next=ListNode(5, next=ListNode(2))))))
out1 = ListNode(1, next=ListNode(2, next=ListNode(2, next=ListNode(4, next=ListNode(3, next=ListNode(5))))))
assert Solution.partition(head=head1, x=3) == out1
"""
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
"""
head2 = ListNode(2, next=ListNode(1))
out2 = ListNode(1, next=ListNode(2))
assert Solution.partition(head=head2, x=2) == out2
"""
Input: head = [2,1], x = 2
Output: [1,2]
"""
