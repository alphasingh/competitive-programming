"""
https://leetcode.com/problems/reverse-linked-list-ii/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, _next=None):
        self.val = val
        self.next = _next

    def __str__(self):
        return str(self.val) + '>' + str(self.next)


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        return ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5)))))


solution = Solution()
example_input = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
assert str(solution.reverseBetween(example_input, 2, 4)) == '1>4>3>2>5>None'
