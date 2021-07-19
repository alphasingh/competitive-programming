"""
https://leetcode.com/problems/reverse-nodes-in-k-group/
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
    def reverseKGroup(head: ListNode, k: int) -> ListNode:
        result = ListNode()
        flat_list = []
        while head:
            flat_list.append(head.val)
            head = head.next
        # print(flat_list)
        head = result
        flat_list_size = len(flat_list)
        for i in range(0, flat_list_size, k):
            sublist = flat_list[i:i + k]
            if len(sublist) == k:
                sublist = sublist[::-1]
            for e in sublist:
                head.next = ListNode(e)
                head = head.next
        return result.next


assert str(Solution.reverseKGroup(head=ListNode(1), k=1)) == str(ListNode(1))

large_list_node = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
assert str(Solution.reverseKGroup(head=large_list_node, k=1)) == '1>2>3>4>5>None'
assert str(Solution.reverseKGroup(head=large_list_node, k=2)) == '2>1>4>3>5>None'
assert str(Solution.reverseKGroup(head=large_list_node, k=3)) == '3>2>1>4>5>None'
