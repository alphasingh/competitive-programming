"""
https://leetcode.com/problems/add-two-numbers/
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
    def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
        addition = ListNode()  # sum = 0
        pointer = addition
        while l1 or l2:
            first = second = carry = 0
            if l1:
                first = l1.val
                l1 = l1.next
            if l2:
                second = l2.val
                l2 = l2.next
            current_sum = first + second + pointer.val
            pointer.val = int(str(current_sum)[-1])  # only last digit
            if current_sum > 9:
                carry = int(str(current_sum)[0])  # first digit
            if carry > 0 or l1 or l2:
                pointer.next = ListNode(carry)
                pointer = pointer.next
        return addition


L1 = ListNode(2, ListNode(4, ListNode(3)))
L2 = ListNode(5, ListNode(6, ListNode(4)))
SUM = ListNode(7, ListNode(0, ListNode(8)))
assert str(Solution.addTwoNumbers(l1=L1, l2=L2)) == str(SUM)
