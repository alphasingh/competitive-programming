"""
https://leetcode.com/problems/sort-list/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val) + '>' + str(self.next)


class Solution:

    @staticmethod
    def convert_to_linked_list(array: [int]) -> ListNode:
        head = ListNode(array[0])
        current = head
        for i in range(len(array) - 1):
            current.next = ListNode(array[i + 1])
            current = current.next
        # print(head)
        return head

    @staticmethod
    def sortList(head: ListNode = None) -> ListNode:
        if not head:
            return head
        current = head
        array = []
        while current:
            array.append(current.val)
            current = current.next
        # print(array, 'sorted', sorted(array))
        return Solution.convert_to_linked_list(sorted(array))


assert str(Solution.sortList(ListNode(4, ListNode(2, ListNode(1, ListNode(3)))))) == '1>2>3>4>None'
assert str(Solution.sortList(ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0))))))) == '-1>0>3>4>5>None'
assert Solution.sortList(None) is None
