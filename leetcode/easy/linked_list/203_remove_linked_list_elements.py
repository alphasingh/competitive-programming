"""
https://leetcode.com/problems/remove-linked-list-elements/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, _next=None):
        self.val = val
        self.next = _next

    def __str__(self):
        return str(self.val) + ">" + str(self.next)


class Solution:

    def removeElements(self, head: 'ListNode', val: int) -> 'ListNode':
        start = ListNode(-1, head)
        pointer = start
        while pointer.next:
            if pointer.next.val == val:  # skip pointer next
                pointer.next = pointer.next.next
            else:
                pointer = pointer.next
        # print(start)
        return start.next


sol = Solution()
assert sol.removeElements(val=7, head=ListNode(7, ListNode(7, ListNode(7, ListNode(7))))) is None
assert sol.removeElements(None, val=19) is None

input_example = ListNode(1, ListNode(2, ListNode(6, ListNode(4, ListNode(5, ListNode(6))))))
output_example = ListNode(1, ListNode(2, ListNode(4, ListNode(5))))
assert str(sol.removeElements(val=6, head=input_example)) == str(output_example)
