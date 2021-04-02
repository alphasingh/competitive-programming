"""
https://leetcode.com/problems/palindrome-linked-list/
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val) + "->" + str(self.next)


class Solution:
    @staticmethod
    def isPalindrome(head: ListNode) -> bool:
        first, second = head, head.next if head else None
        while second:  # if second exists
            if second.val == first.val:
                second = second.next
                first.next = second
            else:  # current_node.val <= start
                first = second
                second = second.next
        return True


assert Solution.isPalindrome(ListNode(
    val=1, next=ListNode(
        val=2, next=ListNode(
            val=2, next=ListNode(
                val=1, next=None))))) is True
assert Solution.isPalindrome(ListNode(
    val=1, next=ListNode(
        val=2, next=None))) is False
