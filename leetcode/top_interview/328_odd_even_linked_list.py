"""
https://leetcode.com/problems/odd-even-linked-list/
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
    def listToNode(array: [int]):
        length = len(array)
        if length == 0:
            return None
        node = ListNode(array[0])
        current = node
        for i in range(length - 1):
            current.next = ListNode(array[i + 1])
            current = current.next
        # print(node)
        return node

    @staticmethod
    def oddEvenList(head: ListNode) -> ListNode:
        position = 0  # starts from odd
        result = [[], []]  # odds, evens
        while head:
            result[position % 2].append(head.val)
            head = head.next
            position += 1
        # print(result)
        result = Solution.listToNode(result[0] + result[1])
        return result


# assert listToNode
assert str(Solution.listToNode([1, 3, 5, 2, 4])) == '1->3->5->2->4->None'
assert str(Solution.listToNode([])) == 'None'

# add TCs for oddEvenList
assert str(Solution.oddEvenList(Solution.listToNode([1, 2, 3, 4, 5]))) == '1->3->5->2->4->None'
assert str(Solution.oddEvenList(Solution.listToNode([2, 1, 3, 5, 6, 4, 7]))) == '2->3->6->7->1->5->4->None'
