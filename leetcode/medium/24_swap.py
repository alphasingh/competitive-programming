"""
https://leetcode.com/problems/simplify-path/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, _next=None):
        self.val = val
        self.next = _next

    def __str__(self):
        return str(self.val) + ">" + str(self.next)


class Solution:
    @staticmethod
    def swapPairs(head: [ListNode]) -> ListNode:
        dummy = ListNode(-1, head)
        curr = dummy
        while curr and curr.next and curr.next.next:
            # initially should have formatted as
            # (zero, one, two, three)
            zero = curr
            one = curr.next
            two = curr.next.next
            three = curr.next.next.next
            # we will swap and make this as
            # (zero, two, one, three)
            zero.next = two
            two.next = one
            one.next = three
            curr = one
        return dummy.next


inl = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
out = ListNode(2, ListNode(1, ListNode(4, ListNode(3))))
assert str(Solution.swapPairs(inl)) == str(out)
inl = None
out = None
assert str(Solution.swapPairs(inl)) == str(out)
inl = ListNode(1)
out = ListNode(1)
assert str(Solution.swapPairs(inl)) == str(out)
"""
[1,2,3,4]
[]
[1]
[1,2,3,4,5,6,7]
[1,3,5]
[1,2]
[1,2,3,4]
[1,2,3,4,5]
[1,2,3,4,5,6]
[1,2,3,4,5,6,7]
[1,2,3,4,5,6,7,8]
[1,2,3,4,5,6,7,8,9]
[1,2,3,4,5,6,7,8,9,10]
"""
