"""
https://leetcode.com/problems/palindrome-linked-list/
"""

from collections import deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val) + "->" + str(self.next)


class Solution:
    @staticmethod
    def isPalindrome(head: ListNode) -> bool:
        elements = deque()
        while head:  # if head exists
            elements.append(head.val)
            head = head.next
        size = len(elements)
        for i in range(size // 2):
            if elements[i] != elements[-i - 1]:
                return False
        return True


assert Solution.isPalindrome(ListNode(
    val=1, next=ListNode(
        val=2, next=ListNode(
            val=2, next=ListNode(
                val=1, next=None))))) is True
assert Solution.isPalindrome(ListNode(
    val=1, next=ListNode(
        val=2, next=None))) is False
assert Solution.isPalindrome(ListNode(
    val=2, next=None)) is True
