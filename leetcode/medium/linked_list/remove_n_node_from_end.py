"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val) + "->" + str(self.next)


class Solution:

    @staticmethod
    def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
        current = head
        size = 0
        while current:  # calculate size
            size += 1
            current = current.next
        # print(head, 'size:', size)
        current = head  # lets start again
        to_be_removed = size - n
        if to_be_removed == 0:
            return head.next
        size = -1
        while current:
            size += 1
            if size == to_be_removed - 1:
                # print("this bro", current.val)
                current.next = current.next.next
                break
            current = current.next
        # print(head)
        return head


linked_list = ListNode(1, next=ListNode(2, next=ListNode(3, next=ListNode(4, next=ListNode(5)))))
assert str(Solution.removeNthFromEnd(head=linked_list, n=2)) == '1->2->3->5->None'
linked_list = ListNode(1, next=ListNode(2, next=ListNode(3, next=ListNode(4, next=ListNode(5)))))
assert str(Solution.removeNthFromEnd(head=linked_list, n=3)) == '1->2->4->5->None'
linked_list = ListNode(1, next=ListNode(2, next=ListNode(3, next=ListNode(4, next=ListNode(5)))))
assert str(Solution.removeNthFromEnd(head=linked_list, n=4)) == '1->3->4->5->None'
linked_list = ListNode(1, next=ListNode(2, next=ListNode(3, next=ListNode(4, next=ListNode(5)))))
assert str(Solution.removeNthFromEnd(head=linked_list, n=5)) == '2->3->4->5->None'

assert str(Solution.removeNthFromEnd(head=ListNode(1, next=ListNode(2)), n=1)) == '1->None'
assert Solution.removeNthFromEnd(head=ListNode(1), n=1) is None
