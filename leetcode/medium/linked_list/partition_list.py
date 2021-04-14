"""
https://leetcode.com/problems/partition-list/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, _next=None):
        self.val = val
        self.next = _next

    def __str__(self):
        return str(self.val) + "->" + str(self.next)


class Solution:
    @staticmethod
    def list_to_node(array: [int]):
        result = None
        size = len(array)
        if size == 0:
            return result
        elif size == 1:
            return ListNode(array[0])
        result = ListNode()
        pointer = result
        for index in range(len(array) - 1):
            pointer.val = array[index]
            pointer.next = ListNode(array[index + 1])
            pointer = pointer.next
        return result

    @staticmethod
    def partition(head: ListNode, x: int) -> ListNode:
        lower = []
        higher = []
        current_node = head
        # create lower and higher
        while current_node:
            value = current_node.val
            if value < x:
                lower.append(value)
            else:
                higher.append(value)
            current_node = current_node.next
        # merge lower and higher
        merged = lower + higher
        # print(merged)
        return Solution.list_to_node(merged)


head1 = ListNode(1, _next=ListNode(4, _next=ListNode(3, _next=ListNode(2, _next=ListNode(5, _next=ListNode(2))))))
out1 = ListNode(1, _next=ListNode(2, _next=ListNode(2, _next=ListNode(4, _next=ListNode(3, _next=ListNode(5))))))
assert str(Solution.partition(head=head1, x=3)) == str(out1)
"""
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
"""
head2 = ListNode(2, _next=ListNode(1))
out2 = ListNode(1, _next=ListNode(2))
assert str(Solution.partition(head=head2, x=2)) == str(out2)
"""
Input: head = [2,1], x = 2
Output: [1,2]
"""
