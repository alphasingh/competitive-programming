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
        elements = []
        while head:  # if head exists
            elements.append(head.val)
            head = head.next
        return elements == elements[::-1]


assert Solution.isPalindrome(ListNode(
    val=1, next=ListNode(
        val=2, next=ListNode(
            val=2, next=ListNode(
                val=1, next=None))))) is True
assert Solution.isPalindrome(ListNode(
    val=1, next=ListNode(
        val=2, next=None))) is False
